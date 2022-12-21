#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


OPS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}
ROPS1 = {
    "+": lambda x, y: x - y,
    "-": lambda x, y: -x + y,
    "*": lambda x, y: x // y,
    "/": lambda x, y: y // x,
}
ROPS2 = {
    "+": lambda x, y: x - y,
    "-": lambda x, y: x + y,
    "*": lambda x, y: x // y,
    "/": lambda x, y: x * y,
}

# part 1
ms = {}
ops = {}
ps = defaultdict(list)
for l in ls:
    idx, m = pa(l, ["{}: {} {} {}", "{}: {i}"])
    if idx == 1:
        ms[m[0]] = m[1]
    else:
        ops[m[0]] = m[1:]
        ps[m[1]].append(m[0])
        ps[m[3]].append(m[0])
q = []
for m in ms:
    q += ps[m]
while q:
    m = q.pop()
    if m in ms:
        continue
    c1, op, c2 = ops[m]
    if c1 in ms and c2 in ms:
        ms[m] = OPS[op](ms[c1], ms[c2])
        q += ps[m]
sm(ms["root"])


# part 2
ms = {}
ops = {}
ps = defaultdict(list)
for l in ls:
    idx, m = pa(l, ["{}: {} {} {}", "{}: {i}"])
    if m[0] == "humn":
        continue
    if idx == 1:
        ms[m[0]] = m[1]
    else:
        ops[m[0]] = m[1:]
        ps[m[1]].append(m[0])
        ps[m[3]].append(m[0])
q = []
for m in ms:
    q += ps[m]
while q:
    m = q.pop()
    if m in ms:
        continue
    c1, op, c2 = ops[m]
    if c1 in ms and c2 in ms:
        ms[m] = OPS[op](ms[c1], ms[c2])
        q += ps[m]
r1, _, r2 = ops["root"]
if r1 in ms:
    k, v = r2, ms[r1]
else:
    k, v = r1, ms[r2]
while k != "humn":
    n1, op, n2 = ops[k]
    if n1 in ms:
        k = n2
        v = ROPS1[op](v, ms[n1])
    else:
        k = n1
        v = ROPS2[op](v, ms[n2])
sm(v)
