# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 14:47:06 2016

@author: leilu
"""

from scipy import spatial

def cosineSimilarity(node1, node2):
    return 1-spatial.distance.cosine(node1.v, node2.v)
    
        
def nearestIndexOnGrid(i, length):
    '''
    rescale integer i into range (0,length) if i is not in this range
    '''
    if i < 0:
        return 0
    elif i >= length:
        return length - 1
    else:
        return i
    
def nearestXYonGrid(x, y, length):
    '''
    find the nearest coordinates (x,y) on the grid 
    if the given (x,y) are not on the grid
    '''
    return nearestIndexOnGrid(x, length), nearestIndexOnGrid(y, length)
