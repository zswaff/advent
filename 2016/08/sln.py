#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
scr = np.zeros((6, 50), int)
for line in lines:
    splt = line.split(' ')
    if line.startswith('rect'):
        a, b = [int(e) for e in splt[1].split('x')]
        scr[0:b, 0:a] = 1
        continue
    if line.startswith('rotate column'):
        col = int(splt[2].split('=')[1]) % 50
        amt = int(splt[4]) % 6
        scr[:, col] = np.concatenate((scr[-amt:, col], scr[:-amt, col]))
        continue
    row = int(splt[2].split('=')[1]) % 6
    amt = int(splt[4]) % 50
    scr[row, :] = np.concatenate((scr[row, -amt:], scr[row, :-amt]))
print(scr.sum())


# part 2
print('\n'.join(''.join('#' if f else ' ' for f in e) for e in scr.tolist()))