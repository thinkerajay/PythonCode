
import functools


def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)

def main():
    tcs = int(input().strip())
    fts = [fact(i) for i in range(1, 10)]
    for _ in range(tcs):
        rear = 8
        yt = list()
        x = int(input().strip())
        while rear > 0 :
            if x < fts[rear]:
                continue
            elif x == fts[rear]:
                print(''.join(yt + [str(rear)]))
            else:
                pass



main()


