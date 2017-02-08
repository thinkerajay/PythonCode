'''
Created on Sep 10, 2016

@author: Admin
'''

from collections import deque


class Node:
    def __init__(self,data):
        self.data = data
        self.left= None
        self.right = None
        self.parent = None
        self.height = 0
        self.leftheight=0
        self.rightheight=0

class Tree:
    def __init__(self):
        print('Tree Constructor Called')
        self._rootnode = None
    def insert(self,data):
        nodeStack = deque()
        if self._rootnode is None:
            print('inserting',data)
            self._rootnode =  Node(data)
            nodeStack.append(self._rootnode)
        else:
            movableNode = self._rootnode
            nodeStack.append(movableNode)
            while True:
                if data > movableNode.data:
                    if movableNode.right is not None:
                        movableNode = movableNode.right
                        nodeStack.append(movableNode)
                    else:
                        print('inserting',data)
                        movableNode.right = Node(data)
                        nodeStack.append(movableNode.right)
                        movableNode.right.parent = movableNode
                        break                        
                else:
                    if movableNode.left is not None:
                        movableNode = movableNode.left
                        nodeStack.append(movableNode)
                    else:
                        print('inserting',data)
                        movableNode.left = Node(data)
                        nodeStack.append(movableNode.left)
                        movableNode.left.parent = movableNode
                        break
        nodeStack2 = nodeStack.__copy__()
        self.reCalculateHeight(nodeStack)
        #self.balancetheTree(nodeStack2)
    
    def rotate(self,node):
        if node.rightheight>node.leftheight:
            self.rotateLeft(node)
        else:
            self.rotateRight(node)
    def rotateLeft(self,node):
        print('rotating left')
        node.right.left = node
        if node.parent is None:
            self._rootnode = node.right
        node.right.parent = node.parent
        node.parent = node.right
        if node.left is not None:
            node.leftheight = node.left.height + 1
        else:
            node.leftheight = 0
        node.right.leftheight+=1       
        node.right.height = max(node.right.leftheight,node.right.rightheight)
        node.rightheight = 0
        node.right = None
        node.height = max(node.leftheight,node.rightheight)
    
    def rotateRight(self,node):
        print('rotating right')
        node.left.right = node
        if node.parent is None:
            self._rootnode = node.left
        node.left.parent = node.parent
        node.parent = node.left
        
        node.leftheight = 0
        if node.right is not None:
            node.rightheight = node.right.height + 1
        else:
            node.rightheight = 0
        node.left.rightheight+=1       
        node.left.height = max(node.left.leftheight,node.left.rightheight)
        node.leftheight = 0
        node.left = None
        node.height = max(node.leftheight,node.rightheight)
    
    def balancetheTree(self,nodeStack):
        
        while nodeStack:
            node = nodeStack.pop()
            print('balancing node',node.data)
            if abs(node.leftheight-node.rightheight)>1:
                self.rotate(node)         
            
    def reCalculateHeight(self,nodeStack):
        prevNode = None        
        while True:
            if not nodeStack:
                break
            if prevNode is None:
                prevNode = nodeStack.pop()
            else:
                currNode = nodeStack.pop()
                if currNode.height<=prevNode.height:
                    currNode.height+=1
                if currNode.data > prevNode.data:
                    currNode.leftheight = prevNode.height+1
                else:
                    currNode.rightheight = prevNode.height+1
                prevNode = currNode
    def display(self):
        if self._rootnode is None:
            raise Exception("No data to display")
        else:
            movableNode = self._rootnode
            nodeStack = deque()
            nodeStack.append(movableNode)
            while True:                
                while True:                    
                    movableNode = movableNode.left
                    if movableNode is None:
                        break                    
                    nodeStack.append(movableNode)                
                movableNode = nodeStack.pop()
                print('data={},height={},leftheight={},rightheight={}'.
                      format(movableNode.data,movableNode.height,movableNode.leftheight,movableNode.rightheight))
                if movableNode.right is None:
                                        
                    if not nodeStack:
                        break
                    movableNode = nodeStack.pop()
                    print('data={},height={},leftheight={},rightheight={}'.
                      format(movableNode.data,movableNode.height,movableNode.leftheight,movableNode.rightheight))
                    while True:
                        if movableNode.right is not None:
                            movableNode = movableNode.right
                            nodeStack.append(movableNode)
                            break
                        else:
                            movableNode = nodeStack.pop()
                            print('data={},height={},leftheight={},rightheight={}'.
                                  format(movableNode.data,movableNode.height,movableNode.leftheight,movableNode.rightheight))
                                 
                    
                else:                    
                    movableNode= movableNode.right
                    nodeStack.append(movableNode)
            
                    
                
                       

def main():
    tree = Tree()
    for data in range(10,60,10):
        tree.insert(data)
    tree.insert(9)
    tree.insert(8)
    
    
  
    tree.display()




















if __name__ == '__main__':
    main()