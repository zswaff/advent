#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
claims = []
for e in lines:
    s = e.split()
    claims.append((
        tuple(int(e) for e in s[2][:-1].split(',')),
        tuple(int(e) for e in s[3].split('x'))
    ))


# part 1
d = np.zeros((1000, 1000), int)
for (x, y), (w, h) in claims:
    d[x:x+w,y:y+h] += 1
print((d >= 2).sum())


# part 2
for i, ((x, y), (w, h)) in enumerate(claims):
    if (d[x:x+w,y:y+h] == 1).all():
        print(i + 1)
