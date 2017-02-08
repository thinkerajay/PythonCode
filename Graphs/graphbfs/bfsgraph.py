'''
Created on Jul 6, 2016

@author: Admin
'''
import queue

class Edge:
    def __init__(self,source,destination):
        source.edges.append(destination)
        destination.edges.append(source)
        self.source =source
        self.destination = destination       
        

class Vertex:
    def __init__(self,name):
        self.name = name
        self.edges = list()
        self.marked=False
        


class BfsGraph:
    def __init__(self):
        self.vertices = list()
        self.edges = list()
        self.bfsQu = queue.Queue().queue
    
    def addVertex(self,v):
        self.vertices.append(v)
    
    def addEdge(self,e):
        self.edges.append(e)
        
    def doBfs(self,start):
        start.marked=True
        self.bfsQu.append(start)
        print(start.name)
        while self.bfsQu:
            v = self.bfsQu.popleft()
            for e in v.edges:
                if not e.marked:
                    e.marked=True  
                    print(e.name)     
                    self.bfsQu.append(e)
        
def main():
    bfsGraph = BfsGraph()
    vObjects = [Vertex(i) for i in range(9)]
    for i in range(9):
        bfsGraph.addVertex(vObjects[i])
    
    e1 = Edge(vObjects[0],vObjects[1])
    e2 = Edge(vObjects[0],vObjects[2])
    e3 = Edge(vObjects[1],vObjects[3])
    e4 = Edge(vObjects[1],vObjects[4])
    e5 = Edge(vObjects[2],vObjects[6])
    e6 = Edge(vObjects[2],vObjects[7])
    e7 = Edge(vObjects[2],vObjects[4])
    e8 = Edge(vObjects[4],vObjects[5])
    e9 = Edge(vObjects[6],vObjects[7])
    e10 = Edge(vObjects[1],vObjects[2])
    e11 = Edge(vObjects[3],vObjects[4])
    
    bfsGraph.addEdge(e1)
    bfsGraph.addEdge(e2)
    bfsGraph.addEdge(e3)
    bfsGraph.addEdge(e4)
    bfsGraph.addEdge(e5)
    bfsGraph.addEdge(e6)
    bfsGraph.addEdge(e7)
    bfsGraph.addEdge(e8)
    bfsGraph.addEdge(e9)
    bfsGraph.addEdge(e10)
    bfsGraph.addEdge(e11)
    
    bfsGraph.doBfs(vObjects[0])
    
main()
    
    
    
    