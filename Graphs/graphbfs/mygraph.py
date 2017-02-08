'''
Created on Dec 29, 2016

@author: Admin
'''


class Vertex:
    def __init__(self, label):
        self.id = label
        self.connectedTo = dict()
    
    
    def addNeighbor(self, vertex):