'''
Created on Dec 18, 2016

@author: Admin
'''



class Edge:
    def __init__(self,source,destination,weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class Vertex:
    def __init__(self,label):
        self.label = label
        self.edges = list()
    
    def getMinEdge(self):
        minEdge = None
        for edge in self.edges:
            if minEdge is None:
                minEdge = edge
            else:
                minEdge = edge if edge.weight < minEdge.weight else minEdge
           
        return minEdge
     


class Graph:
    def __init__(self):
        self.vertices = dict()
        self.edges = list()
    
    def addVertex(self,label):
        vertex = Vertex(label)
        self.vertices[label] = vertex
    
    def addEdge(self,source,destination,weight):
        edge = Edge(source,destination,weight)
        self.edges.append(edge)
        source = self.vertices[source]
        destination = self.vertices[destination]
        source.edges.append(edge)
        destination.edges.append(edge)
    
    def shortPath(self,s,t):
        source = self.vertices[s]
        destination = self.vertices[t]
        
        temp = source
        pathweight = 0
        print(source.label)
        while True:
            minEdge = temp.getMinEdge()
            pathweight += minEdge.weight
            temp = self.vertices[minEdge.destination]
             
        
        
        

graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')

graph.addEdge('a', 'b', 5)
graph.addEdge('b', 'c', 2)
graph.addEdge('c', 'd', 3)
graph.addEdge('d', 'e', 6)
graph.addEdge('e', 'f', 5)
graph.addEdge('f', 'a', 4)
graph.addEdge('a', 'e', 2)











    
    
    
