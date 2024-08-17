# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph

# An edge list is an array or list of edges, where each edge is represented by a pair of vertices (cells) it connects.
class EdgeListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    """
    Represent an undirected graph using an edge list. Each edge is a tuple contain two vertice and option wall status
    """

    def __init__(self):
        ### Implement me! ###
        #initiate a list to store the edges and set to store the vertices
        self.edges: List[tuple[Coordinates, Coordinates, bool]] = []
        self.vertices: set[Coordinates] = set()


        
    def addVertex(self, label:Coordinates):
        ### Implement me! ###
        # Add a vertex to a set of vertices
        self.vertices.add(label)
    


    def addVertices(self, vertLabels:List[Coordinates]):
        ### Implement me! ###
        # Add multiple vertices by extending the set
        for label in vertLabels:
            self.addVertex(label)



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        ### Implement me! ###
        # remember to return booleans
        # Ensure that both vertices are in the graph 
        if vert1 not in self.vertices or vert2 not in self.vertices:
            return False

        # Add the edge if it doesn't exist
        if not self.hasEdge(vert1, vert2):
            self.edges.append((vert1, vert2, addWall))
            return True
        return False
        


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        # Update wall status for an existing edge
        for i, (v1, v2, _) in enumerate(self.edges):
            if(v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                self.edges[i] = (v1, v2, wallStatus)
                return True
        return False
        



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        for i,(v1, v2, _) in enumerate(self.edges):
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 ==vert1):
                self.edges.pop(i)
                return True
        return False
        
        


    def hasVertex(self, label:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        # Check if the vertex exists in the list
        return label in self.vertices
        


    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        # check if the edge exists between 2 vertices 
        return any ((v1 == vert1 and v2 == vert2) or (v2 == vert1 and v1 == vert2) for v1, v2, _ in self.edges)



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        # Get wall status in between 2 vertices if edge exists
        for v1, v2, wallStatus in self.edges:
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                return wallStatus
        return False



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        ### Implement me! ###
        # remember to return list of coordinates
        # Find all neighbour of a given vertex
    
        neighbours = []
        for v1, v2, _ in self.edges:
            if v1 == label:
                neighbours.append(v2)
            elif v2 ==label:
                neighbours.append(v1)
        return neighbours
    
    
     