#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
ns = [[int(f) for f in e.split()] for e in lines]


# part 1
print(sum(max(e) - min(e) for e in ns))


# part 2
r = []
for l in ns:
    sl = sorted(l)
    for i, e in enumerate(sl):
        for f in sl[i + 1:]:
            if f % e == 0:
                r.append(f // e)
print(sum(r))
