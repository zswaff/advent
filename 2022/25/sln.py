#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *

RM = {"-": -1, "=": -2}
RMR = {v: k for k, v in RM.items()}

# part 1
c = 0
for l in ls:
    for i, ch in enumerate(reversed(l)):
        c += (5**i) * int(RM.get(ch, ch))
print(c)
r = ""
for i in count():
    pw = 5**i
    pwh = pw // 2
    if pw - pwh <= c <= (2 * pw) + pwh:
        break
for j in range(i, -1, -1):
    pw = 5**j
    n = round(c / pw)
    c -= n * pw
    r += str(RMR.get(n, n))
sm(r)
