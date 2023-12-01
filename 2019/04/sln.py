#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter


# part 1
c = 0
for i in range(165432, 707912 + 1):
    worked = True
    pair = False
    s = 0
    for e in str(i):
        f = int(e)
        if f < s:
            worked = False
            break
        if f == s:
            pair = True
        s = f
    if pair and worked:
        c += 1
print(c)


# part 2
c = 0
for i in range(165432, 707912 + 1):
    worked = True
    pair = False
    s = 0
    for e in str(i):
        f = int(e)
        if f < s:
            worked = False
            break
        if f == s:
            pair = True
        s = f
    if pair and worked and 2 in set(Counter(str(i)).values()):
        c += 1
print(c)
