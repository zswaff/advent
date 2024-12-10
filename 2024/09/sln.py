#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
f = []
o = True
for i, c in enumerate(dt):
    f += [(i // 2) if o else None] * int(c)
    o = not o
for i, e in enumerate(f):
    if e is not None:
        continue
    while (x := f.pop()) is None:
        continue
    if i >= len(f):
        f.append(x)
        continue
    f[i] = x
sm(sum(i * e for i, e in enumerate(f)))


# part 2
f = []
o = True
for i, c in enumerate(dt):
    f.append([o, int(c), (i // 2) if o else None])
    o = not o
sz = len(f) // 2
for i in range(sz, -1, -1):
    idx, t = next((j, e) for j, e in enumerate(f) if e[2] == i)
    o, x, _ = t
    for j, st in enumerate(f):
        so, sx, si = st
        if si == i:
            break
        if so or sx < x:
            continue
        t[0] = False
        st[1] -= x
        f.insert(j, [o, x, i])
        break
nf = []
for o, x, idx in f:
    nf += [idx if o else None] * x
sm(sum(i * e for i, e in enumerate(nf) if e is not None))
