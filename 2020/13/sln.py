#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
t0 = int(lines[0])
bs = lines[1].split(',')
bsi = [int(e) for e in bs if e != 'x']


# part 1
def bus():
    for i in count(t0):
        for b in bsi:
            if i % b == 0:
                return (i - t0) * b
print(bus())


# part 2
curr = -1
skip = 1
for i, b in enumerate(bs):
    curr += 1
    if b == 'x':
        continue
    b = int(b)
    for j in range(b):
        if curr % b == 0:
            skip *= b
            break
        curr += skip
print(curr - len(bs) + 1)
