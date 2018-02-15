


def isPalindrome(istr):
    return istr == istr[::-1]

def main():
    tcs = int(input().strip())
    for _ in range(tcs):
        n, k = map(int, input().strip().split())
        inputString = input().strip()
        if isPalindrome(inputString):
            if k < len(inputString) - 1:
                print(1)
            else:
                print(0)
        else:
            start = 0
            h = 0
            rear = len(inputString) - 1
            while start < rear:
                if inputString[start] == inputString[rear]:
                    start += 1
                    rear -= 1
                else:
                    pass
main()





