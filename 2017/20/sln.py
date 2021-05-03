#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
ps = [
    [tuple(int(g) for g in f[3:].split(',')) for f in e[:-1].split('>, ')]
    for e in lines
]

def add(a, b):
    return tuple(e + f for e, f in zip(a, b))


# part 1
for _ in range(100000):
    for e in ps:
        e[1] = add(e[1], e[2])
        e[0] = add(e[0], e[1])
print(min(
    range(len(ps)),
    key=lambda x: sum(abs(e) for e in ps[x][0])
))


# part 2
for _ in range(100000):
    d = defaultdict(list)
    for i, e in enumerate(ps):
        e[1] = add(e[1], e[2])
        e[0] = add(e[0], e[1])
        d[e[0]].append(i)
    s = {e for v in d.values() if len(v) > 1 for e in v}
    ps = [e for i, e in enumerate(ps) if i not in s]
print(len(ps))
