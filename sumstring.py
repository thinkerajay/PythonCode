
def isSumString():
    tcs = int(input().strip())

    for _ in range(tcs):
        inputString = input().strip()
        li = len(inputString)
        i = 1
        while True:
            j = int(inputString[-i:])
            k = 0
            while k < i-1:
                if j == int(inputString[li-i]) + int(map(str, inputString[k:li-i])):
                    break
                k += 1
            i += 1


