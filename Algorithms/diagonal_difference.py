#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
#print (a)
primary=0
secondary=0
i=0
while i<n:
    
    primary=primary+a[i][i]
    secondary=secondary+a[i][(n-1)-i]
    i+=1
    
if primary>secondary:
    ans=primary-secondary
else:
    ans=secondary-primary
    

print (ans)
