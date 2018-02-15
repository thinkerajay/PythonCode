
from collections import defaultdict

class Vertex:
    def __init__(self, element):
        self._element = element

    def __hash__(self):
        return hash(id(self))

    def element(self):
        return self._element

class Edge:
    def __init__(self, u, v, e):
        self.source = u
        self.destination = v
        self.element = e

    def points(self):
        return (self.source, self.destination)

    def opposite(self, u):
        return self.source if u is self.destination else self.destination
class Graph:
    def __init__(self):
        self.vertices = dict()
    def insertVertex(self, u):
        vertex = Vertex(u)
        self.vertices[vertex] = dict()
        return vertex

    def insertEdge(self, u, v, e):
        edge = Edge(u, v, e)
        self.vertices[u][v] = edge
        self.vertices[v][u] = edge

    def display(self):
        from pprint import pprint
        pprint(self.vertices)

def main():
    graph = Graph()
    v1 = graph.insertVertex(0)
    v2 = graph.insertVertex(1)
    v3 = graph.insertVertex(2)
    v4 = graph.insertVertex(3)

    graph.insertEdge(v1,v2,1)
    graph.insertEdge(v1,v3,2)
    graph.insertEdge(v2,v4,3)
    graph.insertEdge(v3,v4,4)
    graph.display()

if __name__=='__main__':
    main()












