'''
Created on Sep 4, 2016

@author: Admin
'''
import math
import time
import pprint
from functools import lru_cache

def clock(func):
    def clocked(*args):
        t0=time.time()
        result = func(*args)
        print('it took %s secs'%(time.time()-t0))
        pprint.pprint(result)
        return result
    return clocked

def getDistance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2) 


@clock
def determineClosestPair(p):
    
    pairDict = dict()
    for p1 in p:
        for p2 in p:
            if p2!=p1:
                dist = getDistance(p1, p2)
                pairDict[(p1,p2)] = dist
    minV=None
    closePair = None
    for key,val in pairDict.items():
        if minV is None:
            minV = val
            closePair = key
        else:
            if val<minV:
                minV = val
                closePair = key
    return closePair


def effClosestPair(p):
    p=list(p)
    px = sorted(p,key = lambda x:x[0])
    py = sorted(p,key=lambda x:x[1])
    print(px)
    print(py)
    print('final pair=',effPair(px,py))

def effPair(px,py):
    print(px,'--y--',py)
    if len(px+py)<=3:
        if len(px+py)==2 and px==py:
            return (px[0],py[0])
        else:
            return determineClosestPair(px+py)
    else:
        q0,q1 = effPair(px[:math.ceil(len(px)/2)],py[:math.ceil(len(py)/2)])
        r0,r1=effPair(px[math.ceil(len(px)/2):],py[math.ceil(len(py)/2):])
        print('q0=',q0,'q1=',q1)
        print('r0=',r0,'r1=',r1)
        delta = min(getDistance(q0,q1),getDistance(r0,r1))
        l = sorted([q0]+[q1],key=lambda x:x[0])[1]
        largeX =l[0]
        print('l=',l,'largex=',largeX)
        print(delta)
        if getDistance(q0,q1)<getDistance(r0,r1):
            return q0,q1
        else:
            return r0,r1
        



def main():
    p = set()
    p.add((1,2))
    p.add((2,1))
    p.add((3,4))
    p.add((4,3))   
    
    p.add((5,9))
    
    p.add((9,6))
    
    
    P=list()
    P = [list(ele) for ele in p]
    
    
    
    
    effClosestPair(p)

if __name__ == '__main__':
    main()