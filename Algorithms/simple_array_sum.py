#!/bin/python3

import sys

def simpleArraySum(n, ar):
    # Complete this function
    ans=0
    for each in ar:
        ans= ans + each
    return ans
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
