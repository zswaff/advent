#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict
from itertools import product


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
mask = 'X' * 36

def do_mask(n):
    return int(''.join(
        m if m != 'X' else e
        for m, e in zip(mask, bin(n)[2:].rjust(36, '0'))
    ), 2)

mem = defaultdict(int)
for line in lines:
    cmd, _, val = line.split(' ')
    if cmd == 'mask':
        mask = val
        continue
    mem[int(cmd[4:-1])] = do_mask(int(val))
print(sum(e for e in mem.values()))


# part 2
mask = 'X' * 36
xcount = 36

def do_mask(n):
    combs = list(product(['0', '1'], repeat=xcount))
    res = []
    for comb in combs:
        r = ''
        idx = 0
        for m, e in zip(mask, bin(n)[2:].rjust(36, '0')):
            if m == '0':
                r += e
                continue
            if m == '1':
                r += '1'
                continue
            r += comb[idx]
            idx += 1
        res.append(r)
    return res

mem = defaultdict(int)
for line in lines:
    cmd, _, val = line.split(' ')
    if cmd == 'mask':
        mask = val
        xcount = sum(e == 'X' for e in val)
        continue
    val = int(val)
    for e in do_mask(int(cmd[4:-1])):
        mem[e] = val
print(sum(e for e in mem.values()))
