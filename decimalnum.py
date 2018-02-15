# code

def main():
    tcs = int(input().strip())

    for _ in range(tcs):
        x, y, n = map(int, input().strip().split())
        start = min(x, y)
        m = 0
        print(start,x,y,n)
        for k in range(start, n + 1):
            print(k)
            if k == x or k == y:
                m += 1
                print('in if')
            else:
                if (k % x == 0) or (k % y == 0) or (k % (x + y)) == 0:
                    m += 1
                    print('in else',n)

        print(m)


main()