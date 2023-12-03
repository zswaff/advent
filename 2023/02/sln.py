#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
c = 0
for l in ls:
    idx, rest = l[5:].split(": ")
    idx = int(idx)
    sets = rest.split("; ")
    worked = True
    for s in sets:
        x = s.split(", ")
        r = next((e for e in x if e.endswith(" red")), None)
        g = next((e for e in x if e.endswith(" green")), None)
        b = next((e for e in x if e.endswith(" blue")), None)
        if r is not None and int(r[:-4]) > 12:
            worked = False
            break
        if g is not None and int(g[:-6]) > 13:
            worked = False
            break
        if b is not None and int(b[:-5]) > 14:
            worked = False
            break
    if worked:
        c += idx
sm(c)


# part 2
c = 0
for l in ls:
    idx, rest = l[5:].split(": ")
    idx = int(idx)
    sets = rest.split("; ")
    mr, mg, mb = None, None, None
    for s in sets:
        x = s.split(", ")
        r = next((e for e in x if e.endswith(" red")), None)
        g = next((e for e in x if e.endswith(" green")), None)
        b = next((e for e in x if e.endswith(" blue")), None)
        if r is not None:
            mr = max(mr, int(r[:-4])) if mr is not None else int(r[:-4])
        if g is not None:
            mg = max(mg, int(g[:-6])) if mg is not None else int(g[:-6])
        if b is not None:
            mb = max(mb, int(b[:-5])) if mb is not None else int(b[:-5])
    c += mr * mg * mb
sm(c)
