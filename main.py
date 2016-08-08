# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:13:41 2016

@author: leilu
"""
from GridLocality import GridLocality

grid = GridLocality(5, False)
#print grid.node_retrieval(6)

#grid.getSquareNeighbors(4, 4, 1)
#print grid.getNeighbors(100, 5, 3, 'diamond')
    
#print grid.resourseDistribution( 10, [1,4,7], 2)
    
print grid.findReprentative()