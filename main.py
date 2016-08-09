# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:13:41 2016

@author: leilu
"""
from GridLocality import GridLocality


def main():
	grid = GridLocality(3, True)
	
	#node_info = grid.nodeRetrieval(6)

	#neighbors = grid.getNeighbors(4, 5, 3, 'diamond')
    
	#resource = grid.resourseDistribution( 10, [1,4,7], 2)
    
	winner = grid.findReprentative()
	
	print winner
	
if __name__ == "__main__":
    main()
