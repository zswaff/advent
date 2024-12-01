#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
l1, l2 = [], []
for e in ls:
    a, b = pa(e, "{i}   {i}")
    l1.append(a)
    l2.append(b)
l1.sort()
l2.sort()
sm(sum(abs(e - l2[i]) for i, e in enumerate(l1)))


# part 2
c = Counter(l2)
sm(sum(e * c[e] for e in l1))
