#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
rs, iss = ss
rs = [pa("{i}-{i}", e) for e in rs]
iss = [int(e) for e in iss]
c = 0
for i in iss:
    for mn, mx in rs:
        if mn <= i <= mx:
            c += 1
            break
sm(c)


# part 2
frs = [rs.pop(0)]
while rs:
    cmn, cmx = c = rs.pop(0)
    for i, (mn, mx) in enumerate(frs):
        if min(mx, cmx) >= max(mn, cmn):
            frs.pop(i)
            rs.append((min(mn, cmn), max(mx, cmx)))
            break
    else:
        frs.append(c)
sm(sum(e[1] - e[0] + 1 for e in frs))
