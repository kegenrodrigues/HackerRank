#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    
    # Complete this function
    ans=0
    for each in ar:
        ans= ans + each
    return ans    
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
