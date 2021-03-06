# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:49:39 2016

@author: leilu
"""
import numpy as np
from helper import cosineSimilarity, nearestXYonGrid
import math 

class Node():
    def __init__(self, i, n):
    # i is the index number of the node in the grid, 
    # n is the length of the grid.
        self.i = i
        self.x = i // n
        self.y = i % n
        self.v = np.random.rand(n)
        
    def printInfo(self):
        print "({}, {}, {})".format(self.x, self.y, self.i)
        
    def __str__(self):
        return "coordinates: ({}, {}), i: {}, v: {}".format(self.x, self.y, self.i, self.v)
        
    def isAt(self, center_x, center_y):
        return self.x == center_x and self.y == center_y
        
    def isCrossNeighborOf(self, center_x, center_y):
        return self.x == center_x or self.y == center_y
        
    def isDiamondNeighborOf(self, center_x, center_y, m):
        return abs(self.x - center_x) + abs(self.y - center_y) <= m
    
    def getMagnitude(self):
        return np.linalg.norm(self.v)
        

class GridLocality(object):
    """A list of n*n node objects. 

    Attributes:
        n: a positive integer representing the number of nodes on each side 
        stdout: a boolean variable 
    """
    def __init__(self,n,stdout):  
        self.length = n
        self.grid = []
        for i in range(n * n):
            node = Node(i, n)
            self.grid.append(node)
            if stdout:
                node.printInfo()

            
    def nodeRetrieval(self, index):
        '''
        given the index, return features (x, y, i, v) for the node object
        '''
        return self.grid[index]
       
    def getNode(self, x, y):
        """
        given the coordinates(x,y), return the node object at this coordinates
        """
        if x >= self.length or y >= self.length:
            return None
        i = self.length * x + y
        return self.nodeRetrieval(i)
            
    def getNeighbors(self, x, y, m, n_type):
        '''
        parameters:
        
        x: integer--x coordinate
        y: integer--y coordinate
        m: integer--distance
        n_type: string--type of neighbors
        
        return a lists of node objects that are n_type neighbors of node at (x,y)
        '''
    # n_type is the neighborhood type.         
        x, y = nearestXYonGrid(x, y, self.length)
        neighbors = []
        for neighbor_x in range(max(0, x-m), min(self.length, x+m+1)):
            for neighbor_y in range(max(0, y-m), min(self.length, y+m+1)):
                neighbor =  self.getNode(neighbor_x, neighbor_y)
                if n_type == "square":
                    if not neighbor.isAt(x, y):
                        neighbors.append(neighbor)
                if n_type == "cross":
                    if neighbor.isCrossNeighborOf(x, y) and (not neighbor.isAt(x, y)):
                        neighbors.append(neighbor) 
                if n_type == "diamond":
                    if neighbor.isDiamondNeighborOf(x, y, m) and (not neighbor.isAt(x, y)):
                        neighbors.append(neighbor) 
        return [(node.x, node.y) for node in neighbors]


    def resourseDistribution(self, k, g, strategy):
        '''
        distribute resource to few nodes
        
        parameter: 
        k: integer/float-- the numerical quantity that will be distributed
        g: array-- list of indice 
        startegy: int -- decide distribution method
        
        return a list of floats 
        
        '''            
        if strategy == 1:   
            weight_list = [self.nodeRetrieval(i).getMagnitude() for i in g]
        else:
            weight_list = [self.nodeRetrieval(i).y for i in g]
        total = sum(weight_list)
        normalized_weights = map(lambda x: float(x)/total, weight_list)
        resource_list =  map(lambda x: k*x, normalized_weights)
        return resource_list
       
    def findReprentative(self):
        '''
    
        return the node object that is most similar to other nodes in the grid
        '''
        j = (sum([n.getMagnitude() for n in self.grid])/len(self.grid))/math.sqrt(self.length)
        representative = self.grid[8] #initilize the representative
        rep_AC = 0
        for node in self.grid:
            node_AC = self.findAC(node, j)
            if node_AC > rep_AC:
                representative = node
                rep_AC = node_AC
        return representative
            
            
    def findAC(self, node, j):
        count = 0
        for n in self.grid:
            if cosineSimilarity(n, node) <= j:
                count += 1
        return count
