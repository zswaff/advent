#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from web import *


# part 1
ps = int(dt.split()[0])
mx = int(dt.split()[-2])
d = [0] * ps
c = 0
l = [0]
for i in range(1, mx):
    if i % 23 != 0:
        c = (c + 2) % len(l)
        l.insert(c, i)
    else:
        c = (c - 7) % len(l)
        x = l.pop(c)
        c %= len(l)
        d[i % ps] += i + x
sm(max(d))


# part 2
class Node:
    def __init__(self, v, n, p):
        self.v = v
        self.n = n
        self.p = p

mx *= 100
d = [0] * ps
c = Node(0, None, None)
c.n = c.p = c
for i in range(1, mx):
    if i % 23 != 0:
        c = c.n
        c.n.p = Node(i, c.n, c)
        c.n = c.n.p
        c = c.n
    else:
        c = c.p.p.p.p.p.p
        v = c.p.v
        c.p = c.p.p
        c.p.n = c
        d[i % ps] += i + v
sm(max(d))
