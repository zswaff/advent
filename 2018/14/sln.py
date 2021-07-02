#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from web import *

# part 1
c = int(dt)
r = [3, 7]
e0, e1 = 0, 1
while len(r) < c + 10:
    r += [int(e) for e in str(r[e0] + r[e1])]
    e0 = (e0 + r[e0] + 1) % len(r)
    e1 = (e1 + r[e1] + 1) % len(r)
sm(''.join(str(e) for e in r[c:c + 10]))

# part 2
r = [3, 7]
e0, e1 = 0, 1
l = len(dt)
while True:
    r += [int(e) for e in str(r[e0] + r[e1])]
    t = ''.join(str(e) for e in r[-l - 1:])
    if t[1:] == dt or t[:-1] == dt:
        break
    e0 = (e0 + r[e0] + 1) % len(r)
    e1 = (e1 + r[e1] + 1) % len(r)
sm(len(r) - l - (1 if t[:-1] == dt else 0))
