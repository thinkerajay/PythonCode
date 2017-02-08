'''
Created on Jan 15, 2017

@author: Admin
'''


class StackOverflow(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return super().__str__(self.msg)



class Stack:
    __slots__=['_stack','maxlen']
    def __init__(self, maxlen=5):
        self._stack = list()
        self.maxlen = maxlen
    
    def push(self, value):
        if len(self._stack) == self.maxlen:
            raise Exception('Stack Overflow')
        self._stack.append(value)
    
    def pop(self):
        if len(self._stack)<1:
            raise Exception('Stack Underflow')
        return self._stack.pop()
    
    def __repr__(self):
        return [i for i in self._stack]
    
    def __str__(self):
        return str(self._stack)
    
    def __setattribute__(self, attr,value):
        raise Exception('Private Cannot set')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        