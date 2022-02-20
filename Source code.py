# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:25:13 2022

@author: AK Nahin
"""
lines = []
from collections import Counter
def delete(input):
    input = input.split(" ")
    for i in range(0,len(input)):
        input[i] = "".join(input[i])
    unique = Counter(input)
    s = " ".join(unique.keys())
    return s
c = int(input()); l = []; d = []; out=[]
for i in range(0,c):
    like  = input().split()
    for j in range(1,len(like)):
        l.append(like[j])
    dislike = input().split()
    for j in range(1,len(dislike)):
        d.append(dislike[j])
for i in range(0,len(l)):
    try:
        d.index(l[i])
        continue
    except:
        out.append(l[i])
o = ''
for i in range(0,len(out)):
    o = o+' '+out[i]
o = delete(o)
out = o.split()
output = str(len(out))+' '+o
print(output)