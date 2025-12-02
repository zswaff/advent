#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
rso = [e.split("-") for e in l.split(",")]
rs = []
for mns, mxs in rso:
    while len(mns) != len(mxs):
        nmn = 10 ** len(mns)
        rs.append((mns, str(nmn - 1)))
        mns = str(nmn)
    rs.append((mns, mxs))
c = 0
for mns, mxs in rs:
    mn, mx = int(mns), int(mxs)
    ln = len(mns)
    if ln % 2 != 0:
        continue
    sln = ln // 2
    for i in range(int(mns[:sln]), int(mxs[:sln]) + 1):
        x = int(str(i) * 2)
        if x < mn or x > mx:
            continue
        c += x
sm(c)


# part 2
c2 = set()
for mns, mxs in rs:
    mn, mx = int(mns), int(mxs)
    ln = len(mns)
    for sln in range(1, ln // 2 + 1):
        if ln % sln != 0:
            continue
        m = ln // sln
        for i in range(int(mns[:sln]), int(mxs[:sln]) + 1):
            x = int(str(i) * m)
            if x < mn or x > mx:
                continue
            c2.add(x)
sm(sum(c2))
