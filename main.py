# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:13:41 2016

@author: leilu
"""
from GridLocality import GridLocality


def main():
	grid = GridLocality(5, False)
	
	node_info = grid.nodeRetrieval(6)

	neighbors = grid.getNeighbors(1, 2, 2, 'diamond')
    
	resource = grid.resourseDistribution( 10, [1,2,6], 1)
    
	winner = grid.findReprentative()
	
	print node_info, neighbors, resource, winner
	
if __name__ == "__main__":
    main()
