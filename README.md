# Project Name: GridLocality
This project is to construct a grid object and perform some tasks including node information retrieval, neighbor search, and similarity comparison.

## Author: Lei Lu

### Usage of the Modules:
This repository contains three modules:

  - GridLocality.py
  - helper.py
  - main.py

1) GridLocality.py
> This module contains two classes: 1) Node and 2) Grid.

> - Node class  
> >  The Node class was initialized with 4 attributes *x*, *y*, *i* and *v*, where 
   
   > > * integer *x*: the x coordinate of the node in the grid
   > > - integer *y*: the y coordinate of the node at the grid
   > > - integer *i*: the index of the node, representing the order of node being created in the grid
   > > - vector *v*: a random vector of dimension *n*

> > Under the class Grid, there are 6 functions defined:
> > - *self.printInfo()* will print the features of a node object
> > - *self.__str__* represents the node object as its features *(x, y, i)*
> > - *self.isAt( center_x, center_y)* will take in a coordinate ( center_x, center_y) and return a boolean indicating whether the node object is at this coordinate
> > - *self.isCrossNeighborOf(center_x, center_y)* will return a boolean that indicate whether the node is a cross neighbor of node at *(x,y)*
> > - *self.isDiamondNeighborOf()* will return a boolean that indicate whether the node is a diamond neighbor of node at *(x,y)*
> > - *self.getMagnitude()* will return the magnitude of the vector *v* of this node





> - Grid class 
> > The Grid class is a list of nodes object. It was instantiated with 2 parameters *n* and *stdout*, where 

   
   > >- integer *n*: the length of a *n* by *n* grid.
   > >- boolean *stdout*: when equals to *True*, the class will print the features of each node
   > >
> > Under the class Grid, there are also 6 functions defined:
> > - *self.nodeRetrieval(index)* will return the node object given its index
> > - *self.getNode(x, y)* will return the node object given its coordinates*(x, y)*
> > - *self.getNeighbors(x, y, m, n_type)* will take return a list of all the *n_type* neighbors of node *(x,y)* at the distance *m*.
> > - *self.resourseDistribution( k, g, strategy)(center_x, center_y)* return a list of numbers representing the distribution of number *k*.
> > - *self.findAC()* find the *AC* for the node. This function will be used in procedure *self.findReprentative()*.
> >  - *self.findReprentative()* will return the node that is most similar to all the other nides in the grid*.

2) helper.py

> This module contains 3 procedures that are helper functions.
> > - *cosineSimilarity(node1, node2)* will return the cosine similarity between of vectors *v* of node1 and node2.
> > - *nearestIndexOnGrid(i, length)* will return an integer in the range(0,length-1) if the input *i* is out this range.
> > - *nearestXYonGrid(x, y, length)* will return the x coordinates and the y oordinates that are on the grid but are nearest to the input *x* and *y*.


3) main.py

> The main module instantiated a grid instance and call the functions 1)  grid.nodeRetrieval(), 2)grid.getNeighbors(), 3)grid.resourseDistribution(), and 4)grid.findReprentative().