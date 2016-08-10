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

	return node_info, neighbors, resource, (winner.x, winner.y)
	
if __name__ == "__main__":
    node_info, neighbors, resource, winner = main()
    print "The features of the node are: " + str(node_info)
    print "The neighbors of the node are: " + str(neighbors)
    print "The resource distribution is: " + str(resource)
    print "The winner of this grid is: " + str(winner)
