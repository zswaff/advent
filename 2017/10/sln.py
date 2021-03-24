#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import xor
from functools import reduce

SZ = 256

with open('inp.txt') as fin:
    inp = fin.read().strip()

# part 1
lns = [int(e) for e in inp.split(',')]
pos = 0
l = list(range(SZ))
for skip, ln in enumerate(lns):
    l = l[pos:] + l[:pos]
    l = l[:ln][::-1] + l[ln:]
    l = l[-pos:] + l[:-pos]
    pos = (pos + ln + skip) % SZ
print(l[0] * l[1])

# part 2
lns = ([ord(e) for e in inp] + [17, 31, 73, 47, 23]) * 64
pos = 0
l = list(range(SZ))
for skip, ln in enumerate(lns):
    l = l[pos:] + l[:pos]
    l = l[:ln][::-1] + l[ln:]
    l = l[-pos:] + l[:-pos]
    pos = (pos + ln + skip) % SZ
print(''.join(
    f'{e:0>2x}'
    for e in [reduce(xor, l[i * 16:(i + 1) * 16]) for i in range(16)]))
