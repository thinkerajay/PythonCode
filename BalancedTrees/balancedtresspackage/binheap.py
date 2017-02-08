'''
Created on Dec 29, 2016

@author: Admin
'''


class BuildHead:
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0
    
    def percUp(self, i):      
       
        while (i//2) >0:            
            if self.heaplist[i] < self.heaplist[i//2]:
                self.heaplist[i//2],self.heaplist[i] = self.heaplist[i],self.heaplist[i//2]            
            i = i//2
               
    
    def insert(self, key):
        self.heaplist.append(key)
        self.currentsize +=1
        self.percUp(self.currentsize)
    
    def getMin(self):
        retVal = self.heaplist[1]
        newVal = self.heaplist[self.currentsize]
        self.heaplist[1] = newVal
        self.heaplist.pop()
        self.currentsize -=1
        self.percDown(1)
        return retVal
    
    def minChild(self,i):
        if (i*2)+1 > self.currentsize:
            return i*2
        else:
            return i*2 if self.heaplist[i*2]<self.heaplist[i*2+1] else i*2+1
    
    def percDown(self,i):
        while i*2 <= self.currentsize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i],self.heaplist[mc] = self.heaplist[mc],self.heaplist[i]
            i = mc
    


def main():
    heap = BuildHead()
    heap.insert(9)
    heap.insert(10)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(4)
    heap.insert(3)
    heap.insert(8)
    print(heap.heaplist)
    print(heap.getMin())
    print(heap.heaplist)
    print(heap.getMin())
    print(heap.heaplist)
    print(heap.getMin())
    
if __name__=='__main__':
    main()