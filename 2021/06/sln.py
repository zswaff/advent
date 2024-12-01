#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from web import *


# part 1
c = Counter(int(e) for e in dt.split(","))
for _ in range(80):
    nc = Counter({k - 1: v for k, v in c.items() if k > 0})
    nc[6] += c[0]
    nc[8] = c[0]
    c = nc
sm(sum(c.values()))


# part 2
c = Counter(int(e) for e in dt.split(","))
for _ in range(256):
    nc = Counter({k - 1: v for k, v in c.items() if k > 0})
    nc[6] += c[0]
    nc[8] = c[0]
    c = nc
sm(sum(c.values()))
