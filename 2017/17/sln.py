#!/usr/bin/env python3
# -*- coding: utf-8 -*-


INP = 380


# part 1
c = 0
l = [0]
for i in range(2017):
    c = (c + INP) % (i + 1) + 1
    l.insert(c, i + 1)
print(l[c + 1])


# part 2
c = 0
n = 1
for i in range(int(5e7)):
    c = (c + INP) % (i + 1) + 1
    if c == 1:
        n = i + 1
print(n)
