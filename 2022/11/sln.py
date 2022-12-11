#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
ms = []
for _, its, op, tst, ift, iff in ss:
    its = [int(e) for e in its.split(": ")[-1].split(", ")]
    op = op.split("= ")[-1]
    plus = "+" in op
    if plus:
        op = op.split(" + ")
    else:
        op = op.split(" * ")
    sec = False if op[-1] == "old" else int(op[-1])
    tst = int(tst.split(" ")[-1])
    ift = int(ift.split(" ")[-1])
    iff = int(iff.split(" ")[-1])
    ms.append([its, [0], plus, sec, tst, ift, iff])

for _ in range(20):
    for its, ct, plus, sec, tst, ift, iff in ms:
        while its:
            it = its.pop(0)
            if plus:
                nit = (it + (sec if sec is not False else it)) // 3
            else:
                nit = (it * (sec if sec is not False else it)) // 3
            if nit % tst == 0:
                ms[ift][0].append(nit)
            else:
                ms[iff][0].append(nit)
            ct[0] += 1
r = sorted(e[1][0] for e in ms)
sm(r[-1] * r[-2])


# part 2
ms = []
for _, its, op, tst, ift, iff in ss:
    its = [int(e) for e in its.split(": ")[-1].split(", ")]
    op = op.split("= ")[-1]
    plus = "+" in op
    if plus:
        op = op.split(" + ")
    else:
        op = op.split(" * ")
    sec = False if op[-1] == "old" else int(op[-1])
    tst = int(tst.split(" ")[-1])
    ift = int(ift.split(" ")[-1])
    iff = int(iff.split(" ")[-1])
    ms.append([its, [0], plus, sec, tst, ift, iff])

md = lcm(*[e[4] for e in ms])
for bloop in range(10000):
    for its, ct, plus, sec, tst, ift, iff in ms:
        while its:
            it = its.pop(0)
            if plus:
                nit = (it + (sec if sec is not False else it)) % md
            else:
                nit = (it * (sec if sec is not False else it)) % md
            if nit % tst == 0:
                ms[ift][0].append(nit)
            else:
                ms[iff][0].append(nit)
            ct[0] += 1
r = sorted(e[1][0] for e in ms)
sm(r[-1] * r[-2])
