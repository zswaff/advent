#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count

from comp import Comp


# part 1
c = 0
for x in range(50):
    for y in range(50):
        cmp = Comp(fname="inp.txt")
        c += cmp.add_inputs([x, y]).last_outputs[0]
print(c)


# part 2
def ib(x, y):
    return bool(Comp(fname="inp.txt").add_inputs([x, y]).last_outputs[0])


x, y = 1000, 1000
for x in count(x):
    if ib(x, y):
        break
old = x, y
while True:
    for y in count(y, -1):
        if not ib(x + 99, y - 100):
            break
    for x in count(x, -1):
        if not ib(x - 1, y):
            break
    if (x, y) == old:
        break
    old = x, y
m = x + y, x, y
for dx in range(20):
    for dy in range(20):
        if ib(x - dx, y - dy) and ib(x - dx + 99, y - dy - 99):
            m = min(m, (x - dx + y - dy, x - dx, y - dy))
print(m[1] * 10000 + m[2] - 99)
