#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import inf
from collections import defaultdict


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
d = defaultdict(int)
for line in lines:
    uk, iod, amt, _, ck, cop, cv = line.split(" ")
    if not eval(f"{d[ck]} {cop} {cv}"):
        continue
    d[uk] += int(amt) * (1 if iod == "inc" else -1)
print(max(d.values()))


# part 2
m = -inf
d = defaultdict(int)
for line in lines:
    uk, iod, amt, _, ck, cop, cv = line.split(" ")
    if not eval(f"{d[ck]} {cop} {cv}"):
        continue
    d[uk] += int(amt) * (1 if iod == "inc" else -1)
    m = max(m, d[uk])
print(m)
