from collections import defaultdict
def main():
    tcs = int(input().strip())
    for _ in range(tcs):
        n, m = [int(i) for i in input().strip().split()]
        inputList = [int(i) for i in input().strip().split()]
        res = defaultdict(int)
        for i in range(0,len(inputList), 2):
            res[inputList[i]] += 1

        print(sum(res.values()))


main()