'''
Created on May 1, 2016

@author: Admin
'''
from collections import OrderedDict

def gettingDigits(tc,fileOut,inputStr):
    inputStr = inputStr.strip().lower()
    valuesDict = dict(one=1,zero=0,two=2,three=3,four=4,five=5,
                      six=6,seven=7,eight=8,nine=9)
    numberDict = OrderedDict()
    numberDictTwo = OrderedDict()
    numberDict['two'] = ['w']
    numberDict['zero'] = ['z']
    numberDict['six'] = ['x']
    numberDict['four']=['u']
    numberDict['eight']=['g']
    numberDict['five'] = ['v','f']
    numberDict['seven'] = ['v','s']
    numberDictTwo['one'] = ['o','n','e']
    numberDictTwo['three'] = ['t','h','r','e','e']
    numberDictTwo['nine']=['n','i','n','e']
    inputList = list(inputStr.strip())
    #print(numberDict)
    outputList= list()
    for key,value in numberDict.items():
        while True:
            counter = 0
            for alph in value:
                if alph in inputList:
                    counter+=1
            #print('va',value)
            if counter==len(value):
                outputList.append(key)
                #print('key2',key)
                for alph in key:
                    inputList.remove(alph)
            else:
                break
    #print(inputList)
    if len(inputList) >0:
        for key,value in numberDictTwo.items():
            while True:
                counter = 0
                for alph in value:
                    if alph in inputList:
                        counter+=1
                if counter==len(value):
                    #print('key',key)
                    outputList.append(key)
                    for alph in key:
                        inputList.remove(alph)
                else:
                    break
    #print(outputList)
    numberList = list()
    for nb in outputList:
        numberList.append(valuesDict.get(nb))
    numberList = list(map(str,numberList))
    numberList.sort()
    fileOut.write('Case #{}: {}\n'.format(tc,''.join(numberList)))

def main():
    fileIn = open(r'D:\SpyderWorkspace\roundOneB\A-large-practice (2).in','r')
    fileOut=open(r'D:\SpyderWorkspace\roundOneB\A-large-practice (2).out','w')
    ntcs = int(fileIn.readline().strip('\n'))
    for tc in range(1,ntcs+1):
        inputStr = fileIn.readline().strip('\n')
        gettingDigits(tc,fileOut,inputStr)
    fileIn.close()
    fileOut.flush()
    fileOut.close()
    
main()
