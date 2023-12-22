#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
g = set()
bs = []
for l in ls:
    s, f = l.split("~")
    s = [int(e) for e in s.split(",")]
    f = [int(e) for e in f.split(",")]
    for i in range(3):
        if s[i] != f[i]:
            break
    mni, mxi = min(s[i], f[i]), max(s[i], f[i])
    x = [tuple(s[k] if k != i else j for k in range(3)) for j in range(mni, mxi + 1)]
    g |= set(x)
    bs.append(x)

changed = True
while changed:
    changed = False
    for i, b in enumerate(bs):
        sb = set(b)
        g -= sb
        changed_inner = False
        for j in count(1):
            nb = [(e[0], e[1], e[2] - j) for e in b]
            if any(e[2] < 1 or e in g for e in nb):
                break
        if j > 1:
            changed_inner = True
            changed = True
            nb = [(e[0], e[1], e[2] - j + 1) for e in b]
            g |= set(nb)
            bs[i] = nb
        else:
            g |= sb


c = 0
for x in bs:
    sx = set(x)
    g -= sx
    for b in bs:
        if b == x:
            continue
        sb = set(b)
        g -= sb
        nb = [(e[0], e[1], e[2] - 1) for e in b]
        fell = all(e[2] > 0 and e not in g for e in nb)
        g |= sb
        if fell:
            break
    else:
        c += 1
    g |= sx
sm(c)


# part 2
c = 0
for i, x in enumerate(bs):
    ng = {e for e in g if e not in x}
    changed = True
    fell = {i}
    while changed:
        changed = False
        for j, b in enumerate(bs):
            if j in fell:
                continue
            sb = set(b)
            ng -= sb
            nsb = {(e[0], e[1], e[2] - 1) for e in b}
            if any(e[2] < 1 or e in ng for e in nsb):
                ng |= sb
            else:
                changed = True
                fell.add(j)
                ng |= nsb
    c += len(fell) - 1
sm(c)
