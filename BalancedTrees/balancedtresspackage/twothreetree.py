'''
Created on Sep 18, 2016

@author: Admin
'''
class Node:
    def __init__(self):
        self.data = list()
        self.leftpointer = None
        self.rightpointer = None
        self.midpointer = None
        self.parent = None
        
class TwoThreeTree:
    def __init__(self):
        self.rootNode = None
    
    def insert(self,data):
        if self.rootNode is None:
            self.data.append(data)
        else:
            movableNode = self.rootNode
            
            
                    
                