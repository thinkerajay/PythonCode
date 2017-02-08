'''
Created on Dec 29, 2016

@author: Admin
'''
import pprint
from collections import defaultdict
from itertools import chain
class Edge:
    def __init__(self, source, sink, weight):
        self.source = source
        self.sink = sink
        self.weight = weight


def main():
    startVertex = 'a'
    with open('graphdata','r') as fp:
        nVertices = int(fp.readline())
        
        vertices = defaultdict(list)
        for line in fp.readlines():
            source, sink, weight = line.strip().split()
            weight = int(weight)            
            vertices[source].append({sink:weight})
            vertices[sink].append({source:weight})
    d = dict()
    d[startVertex] = 0
    for key in vertices.keys():
        if key!=startVertex:
            d[key] = -1
    
    
    print(d)
    currentVertex = startVertex
    fromVer = startVertex
    for _ in range(nVertices):
        edgeList = vertices[currentVertex]
        for edge in edgeList:
            for key,value in edge.items():
                if key in vertices:
                    if d[key]==-1:
                        d[key] = value
                    else:
                        if d[currentVertex]+value < d[key]:
                            d[key] = d[currentVertex] + value
           
        edges = chain(*[edge.keys() for edge in edgeList if edge!=fromVer and edge!=startVertex])                
        
        fromVer = currentVertex
        print('frome',fromVer)
        currentVertex = min([(edge,d[edge]) for edge in edges],key=lambda x:x[1])
        currentVertex = currentVertex[0]
        print(currentVertex)
            
        
        
    pprint.pprint(vertices)
    pprint.pprint(d)


if __name__=='__main__':
    main() 