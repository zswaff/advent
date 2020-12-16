#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


with open('inp.txt') as fin:
    sec1, sec2, sec3 = [
        e.split('\n')
        for e in fin.read().strip().split('\n\n')
    ]

rules = {}
for e in sec1:
    loc, rngs = e.split(': ')
    rules[loc] = tuple(
        tuple(int(f) for f in e.split('-'))
        for e in rngs.split(' or ')
    )
my_tic = [int(e) for e in sec2[1].split(',')]
nearby = [[int(f) for f in e.split(',')] for e in sec3[1:]]


# part 1
t = 0
for tic in nearby:
    for e in tic:
        if not any(
            mn1 <= e <= mx1 or mn2 <= e <= mx2
            for (mn1, mx1), (mn2, mx2) in rules.values()
        ):
            t += e
print(t)


# part 2
fs = [set(rules.keys()) for _ in range(len(my_tic))]
for tic in nearby + [my_tic]:
    for i, e in enumerate(tic):
        f = {
            k for k, ((mn1, mx1), (mn2, mx2)) in rules.items()
            if mn1 <= e <= mx1 or mn2 <= e <= mx2
        }
        if not f:
            continue
        fs[i] &= f
l = [None for _ in range(len(my_tic))]
while True:
    for i, f in enumerate(fs):
        if len(f) != 1:
            continue
        g = list(f)[0]
        l[i] = g
        for e in fs:
            e -= {g}
    if all(e is not None for e in l):
        break
print(math.prod(e for f, e in zip(l, my_tic) if f.startswith('departure')))
