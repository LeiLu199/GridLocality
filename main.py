# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:13:41 2016

@author: leilu
"""
from GridLocality import GridLocality

grid = GridLocality(2,True)
#grid.Node_retrieval(6)

#print grid.Find_neighbor(4, 4, 3, 'diamond')
    
#print grid.Resourse_distribution( 10, [1,4,7], 2)
    
print grid.Find_reprentative()