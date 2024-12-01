#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *

# part 1
c = 0
for l in ls:
    x = len(l) // 2
    a = list(set(l[:x]) & set(l[x:]))[0]
    c += (ord(a) - ord("A") + 27) if a.isupper() else (ord(a) - ord("a") + 1)
sm(c)


# part 2
c = 0
for i in range(0, len(ls), 3):
    a = list(set(ls[i]) & set(ls[i + 1]) & set(ls[i + 2]))[0]
    c += (ord(a) - ord("A") + 27) if a.isupper() else (ord(a) - ord("a") + 1)
sm(c)
