# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------

import time
from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class IncMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        ### Implement me! ###
        # Initiate vertices list, edges list and incidence matrix
        self.vertices: dict[Coordinates, int] = {}              # Maps the coordinates to vertex index
        self.edges: List[tuple[Coordinates, Coordinates, bool]] = []  # list of edges
        self.incidence_matrix: List[List[int]] = []             # list of incidence



    def addVertex(self, label:Coordinates):
        ### Implement me! ###
        # Add a vertex if it does not exist and update the incidence matrix
        if label not in self.vertices:
            vertex_index = len(self.vertices)
            self.vertices[label] = vertex_index

            # for row in self.incidence_matrix:
            #     row.append(0) 
            # this indicate that a new added vertex does not connect to any of existing vertices
            # A new added row to the incidence matrix
            # This row is initialised with zeros, where number of zeros correspond to number of edges
            self.incidence_matrix.append([0]* len(self.edges)) 



    def addVertices(self, vertLabels:List[Coordinates]):
        ### Implement me! ###
        # Add multiple vertex at once
        for label in vertLabels:
            self.addVertex(label)



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        ### Implement me! ###
        # remember to return booleans
        # Add an edge between two vertices and update the incidence matrix
        # Ensure both vertices exist in the graph
        if vert1 not in self.vertices or vert2 not in self.vertices:
            return False
        # Check if the edge already exists
        if self.hasEdge(vert1, vert2):
            return False
        
        # Add the edge to the list of edges, including the wall status
        self.edges.append((vert1, vert2, addWall))
        edge_index = len(self.edges) - 1 # Index of the newly added edge

        # Expand the incidence matrix: Add a new column for this edge
        for row in self.incidence_matrix:
            row.append(0)
        # Update the incidence matrix
        self.incidence_matrix[self.vertices[vert1]][edge_index] = 1
        self.incidence_matrix[self.vertices[vert2]][edge_index] = 1   
        return True
        
    


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        # timer for generation
		
        startGenTime : float = time.perf_counter()

        for i, (v1,v2,_) in enumerate(self.edges):
            if (v1 == vert1 and v2 == vert2) or (v2 == vert1 and v1 == vert2):
                self.edges[i] = (v1, v2, wallStatus)
                endGenTime: float = time.perf_counter()

                print(f'Update Wall took {endGenTime - startGenTime:0.4f} seconds')
                return True
        # stop timer
        endGenTime: float = time.perf_counter()

        print(f'Update Wall took {endGenTime - startGenTime:0.4f} seconds')
        return False
            



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        # Remove and edge and update the incidence
        for i, (v1,v2,_) in enumerate(self.edges):
            if (v1 == vert1 and v2 == vert2) or (v2 == vert1 and v1 == vert2):
                self.edges.pop(i)
                # Delete the edge in every single row
                for row in self.incidence_matrix:
                    row.pop(i)
                return True
        return False
 


    def hasVertex(self, label:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return label in self.vertices
            


    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        # Check if an edge is exist between two vertices
        return any((v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1) for v1, v2, _ in self.edges)



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        for v1,v2,wall_status in self.edges:
            if (v1 == vert1 and v2 == vert2) or (v2 == vert1 and v1 == vert2):
                return wall_status
        return False


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        ### Implement me! ###
        # remember to return list of coordinates
        # Return a list of neighbours of a given vertex
        # timer for generation
		
        startGenTime : float = time.perf_counter()
        neighbours = []
        if label in self.vertices:
            vertex_index = self.vertices[label]
            for edge_index, (v1,v2, has_wall) in enumerate(self.edges):
                if self.incidence_matrix[vertex_index][edge_index] == 1 :
                    if  v1 == label:
                        neighbours.append(v2)
                    else:
                        neighbours.append(v1)
        # stop timer
		
        endGenTime: float = time.perf_counter()
        print(f'Neighbour took {endGenTime - startGenTime:0.4f} seconds')

        return neighbours
    

        