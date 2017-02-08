'''
Created on Jul 10, 2016

@author: Admin
'''
import queue
class Node:
    def __init__(self,label):
        self.label = label
        self.right = None
        self.left = None
        self.parent = None

class PQTree:
    def __init__(self):
        self.nodes = 0
        self.rootNode = None
        self.pq = queue.Queue().queue
    
    def addNode(self,label):
        if self.rootNode is None:
            self.rootNode = Node(label)
            self.pq.append(self.rootNode)
        else:
            movableNode = self.pq.popleft()         
                    
            if movableNode.left is None:
                if label > movableNode.label:
                    newNode = Node(label)
                    newNode.left = movableNode
                    movableNode.parent = newNode
                movableNode.left = Node(label)
                self.pq.append(movableNode.left)
            elif movableNode.right is None:
                movableNode.right = Node(label)
                self.pq.append(movableNode.right)
            
    def displayTree(self):
        mypq = queue.Queue().queue
        movableNode = self.rootNode
        mypq.append(movableNode)
        while mypq:
            nd = mypq.popleft()
            print(nd.label)
            if nd.left:
                mypq.append(nd.left)
            if movableNode.right:
                mypq.append(nd.right)
            
                


def buildPQ():
    inputNumbers = [2,6,7,9,4,1]
    pqTree = PQTree()
    for ip in inputNumbers:
        pqTree.addNode(ip)
    pqTree.displayTree()
    
buildPQ()