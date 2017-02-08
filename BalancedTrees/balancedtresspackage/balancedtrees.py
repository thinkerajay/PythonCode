'''
Created on Jul 3, 2016

@author: Admin
'''


# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:48:16 2015

@author: Admin
"""
class Node:
    def __init__(self,string):
        self._data = string
        self._leftnode = None
        self._rightnode = None
        self._level = None
    def insert(self,string): 
        currentnode = self
        if string < currentnode._data:            
            while currentnode._leftnode != None:
                currentnode = currentnode._leftnode                        
        else:            
            while currentnode._rightnode != None:
                currentnode = currentnode._rightnode
            
        if string < currentnode._data:
            currentnode._leftnode = Node(string)
            currentnode._leftnode._level = currentnode._level + 1
        else:
            currentnode._rightnode = Node(string)
            currentnode._rightnode._level = currentnode._level + 1  
        
        
class Tree:
    def __init__(self,string):
        self.root = Node(string)
        self.root._level = 0
    def insert(self,string):
        self.root.insert(string)
    def display(self):
        self.__displaytree(self.root)
    def getMin(self):
        pointer = self.root
        while True:
            if pointer._leftnode == None:
                break
            else:
                pointer = pointer._leftnode
        return pointer._data
    def getMax(self):
        pointer = self.root
        while True:
            if pointer._rightnode == None:
                break
            else:
                pointer = pointer._rightnode
        return pointer._data
                  
    def display_data_at_level(self,level):
        self.__display_data_at_level(self.root,level)
    def __display_data_at_level(self, pointer, level):
        if pointer == None:
            return
        else:
            self.__display_data_at_level(pointer._leftnode, level)
            if level == pointer._level:
                print(pointer._data)
            self.__display_data_at_level(pointer._rightnode, level)
        
    def __displaytree(self, pointer):       
        if pointer == None:
            return
        else:            
            self.__displaytree(pointer._leftnode)
            print(pointer._data ,pointer._level)
            self.__displaytree(pointer._rightnode)
        
if __name__ == '__main__':
    firstTree = Tree(0)
    for i in range(10):
        firstTree.insert(i)    
    firstTree.display()
    
    

    
    
    