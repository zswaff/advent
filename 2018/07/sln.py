#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict
from itertools import count

from web import *


# part 1
par = defaultdict(set)
for l in ls:
    spl = l.split()
    par[spl[-3]].add(spl[1])
    par[spl[1]] |= set()
res = []
while par:
    n = min(k for k, v in par.items() if not v)
    par.pop(n)
    res.append(n)
    for s in par.values():
        s -= {n}
sa(''.join(res))


# part 2
cld = defaultdict(set)
par = defaultdict(set)
for l in ls:
    spl = l.split()
    par[spl[-3]].add(spl[1])
    cld[spl[1]].add(spl[-3])
    par[spl[1]] |= set()
done = set()
running = {}
ready = sorted(k for k, v in par.items() if not v)
for i in count():
    ks = list(running.keys())
    for k in ks:
        running[k] -= 1
        if running[k] == 0:
            running.pop(k)
            done.add(k)
            ready += sorted(cld[k])
    while ready:
        if len(running) >= 5:
            break
        k = ready.pop(0)
        if not par[k] <= done:
            continue
        print(k,end='')
        running[k] = 61 + ord(k) - ord('A')
    if not running:
        print()
        break
sb(i)
