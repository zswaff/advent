#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


st = {i for i, e in enumerate(ls[0].split()[-1]) if e == '#'}
lst = len(st)
rs = {}
for l in ls[2:]:
    k, v = l.split(' => ')
    rs[tuple(e == '#' for e in k)] = v == '#'


# part 1
d = {e for e in st}
for i in range(20):
    d = {
        j for j in range(min(d) - 2, max(d) + 3)
        if rs.get(tuple((j + k) in d for k in range(-2, 3)))
    }
sm(sum(d))


# part 2
d = {e for e in st}
ls = 0
ds = 0
for i in count():
    d = {
        j for j in range(min(d) - 2, max(d) + 3)
        if rs.get(tuple((j + k) in d for k in range(-2, 3)))
    }
    nls = sum(d)
    nds = nls - ls
    if nds == ds:
        break
    ls, ds = nls, nds
sm(ls + ds * (int(5e10) - i))
