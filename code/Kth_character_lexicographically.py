#!/usr/bin/python3.8

if __name__ == "__main__":
    N = int(input())
    Q = int(input())
    S = [[s for s in input().split()]]    
    for q in range(0,N-1):
            
    # print("Total Cases {}".format(cases))
    for case in range(cases):
        n = int(input())
        # print("{} Case has {} numbers".format(case+1, n))
        numbers = [int(i) for i in input().split()]
        print(getMagicPairCount(numbers, n))