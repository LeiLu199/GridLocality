# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:49:39 2016

@author: leilu
"""
import numpy as np
from helper import Cosine_similarity

class GridLocality(object):
    """A n x n grid board. 

    Attributes:
        n: a positive integer representing the number of nodes on each side 
        stdout: a boolean variable 
    """
    def __init__(self,n,stdout):
        """
        Return a grid object whose length is n and stdout is stdout
        """
    
        self.length = n
        self.stdout = stdout

    def Construct(self):
        board = []
        for row in range(self.length):
            board.append([])
            for column in range(self.length):
                board[row].append('o')
        
        return board
  
    def Node_info(self):
        if self.stdout == True:
            node_info_dict = {}
            i = 0
            for row in self.Construct():
                for node in row:
                    v = np.random.rand(self.length)
                    i += 1
                    if i%self.length != 0:
                        x = i%self.length
                        y = self.length-i/self.length
                    else:
                        x = self.length
                        y = self.length-i/self.length+1
                    node_info_dict[i] = (x,y,i,v)
                    #print (x,y,i)
                    
            return node_info_dict
            
    def Node_retrieval(self,index):
       return self.Node_info()[index]
    
    def Ingrid(self, node):
        """
        check if a node is on the grid
        
        parameter: node--tuple that represents the coordinates of the node
        output: a boolean indicates whether the node is on the grid
        """
        
        if node[0] in range(1, self.length+1) and node[1] in range(1, self.length+1):
            return True
        else:
            return False
            
    def Get_square_neighbor(self, (x,y)):
        '''
        return a set of square nodes of a given bode, adjacency list
        '''
        neighbors = [(x+1,y),(x+1,y+1),(x,y+1),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y+1),(x-1,y)]
        legal_neighbors = filter(lambda b: self.Ingrid(b)==True, neighbors)        
        return legal_neighbors
   
    def Get_diamond_neighbor(self, (x,y)):
        '''
        return a set of square nodes of a given bode, adjacency list
        '''
        neighbors = [(x+1,y),(x,y+1),(x,y-1),(x-1,y)]
        legal_neighbors = filter(lambda b: self.Ingrid(b)==True, neighbors)        
        return legal_neighbors
        
    def Find_neighbor(self, x, y, m, neighbor_type):
        """
        parameter:
        x: integer--x coordinate
        y: integer--y coordinate
        m: distance
        neighbor_type: string--'square','diamond','cross'
        Return a lists of all neighbor coordinates
        """
        neighbor_list = []
        center = (x, y)
        if m > self.length:
            return neighbor_list
        else:
            if self.Ingrid(center):#center is on the grid
                if neighbor_type == 'cross':
                    i = 1
                    while i <= m:
                        if self.Ingrid((x+i,y)):
                            neighbor_list.append((x+i,y))
                        if self.Ingrid((x-i,y)):
                            neighbor_list.append((x-i,y))
                        if self.Ingrid((x,y+i)):
                            neighbor_list.append((x,y+i))
                        if self.Ingrid((x,y-i)):
                            neighbor_list.append((x,y-i))
                        i += 1
        
              
                if neighbor_type == 'square':
                    #intialize the distance 
                    distance_dict = {}
                    for x_cor in range(1,self.length+1):
                        for y_cor in range(1,self.length+1):
                            distance_dict[(x_cor,y_cor)] = -1
                        
                    distance_dict[(x,y)] = 0  
                    
                    queque = []
                    queque.append(center)
                    
                    
                    while queque:
                        current = queque[0]
                        
                        queque.pop(0)
                        
                        
                        for neighbor in self.Get_square_neighbor(current):
                            
                            if distance_dict[neighbor]==-1:
                                distance_dict[neighbor] = distance_dict[current]+1
                                neighbor_list.append(neighbor)
                                if distance_dict[neighbor]< m:
                                    queque.append(neighbor)

                if neighbor_type == 'diamond':
                    distance_dict = {}
                    for x_cor in range(1,self.length+1):
                        for y_cor in range(1,self.length+1):
                            distance_dict[(x_cor,y_cor)] = -1
                        
                    distance_dict[(x,y)] = 0  
                    
                    queque = []
                    queque.append(center)
                    
                    
                    while queque:
                        current = queque[0]
                        
                        queque.pop(0)
                        
                        
                        for neighbor in self.Get_diamond_neighbor(current):
                            
                            if distance_dict[neighbor]==-1:
                                distance_dict[neighbor] = distance_dict[current]+1
                                neighbor_list.append(neighbor)
                                if distance_dict[neighbor]< m:
                                    queque.append(neighbor)
            #else:
                
     

        return neighbor_list

    def Resourse_distribution(self, k, g, strategy):
        '''
        distribute resource to few nodes
        
        parameter: 
        k: integer/float-- the numerical quantity that will be distributed
        g: array-- list of indice 
        startegy: int -- decide distribution method
        
        '''
        
        vector_list = map(lambda x: self.Node_retrieval(x)[-1], g)
        magnitude_list = map(lambda x: np.linalg.norm(x), vector_list)
        total_magnitude = sum(magnitude_list)
        weight_list_1 = map(lambda x: float(x)/total_magnitude, magnitude_list)
            
        y_list = map(lambda x: self.Node_retrieval(x)[1], g)
        total_y = sum(y_list)
        weight_list_2 = map(lambda x: float(x)/total_y, y_list)
            
        if strategy == 1:            
            resource_list =  map(lambda x: k*x, weight_list_1)
        else:
            resource_list =  map(lambda x: k*x, weight_list_2)
        
        return resource_list
       
    def Find_reprentative(self):
        magnitude_list = []
        for index in range(1,self.length**2+1):
            magnitude = np.linalg.norm(self.Node_retrieval(index)[-1])
            magnitude_list.append(magnitude)
        
        j = np.mean(magnitude_list)
        
        max_AC = 0
        winner = 8 #initilize winner as the first node
        for i in range(1,(self.length)**2+1):
            nodeA_vector = self.Node_retrieval(i)[-1]
            AC = 0
            for r in range(1,(self.length)**2+1):
                if r != i:
                    other_vector = self.Node_retrieval(r)[-1]
                    similarity = Cosine_similarity(nodeA_vector,other_vector)
                    if similarity <= j:
                        AC += 1
            
                    
            if AC > max_AC:
                max_AC = AC
                winner = i
        
        return winner,max_AC,j