#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
WRAPS = [(1, min), (0, min), (1, max), (0, max)]

rg, ro = ss
g = {k: v for k, v in gr(rg, lambda x: None if x == " " else x == "#").items() if v is not None}
os = []
for c in ro[0]:
    if c.isdigit():
        if os and isinstance(os[-1], int):
            os[-1] = int(os[-1]) * 10 + int(c)
        else:
            os.append(int(c))
    else:
        os.append(c)


# part 1
y = min(e[1] for e in g)
x = min(e[0] for e in g if e[1] == y and not g[e])
f = 0
for o in os:
    if o == "R":
        f = (f + 1) % 4
        continue
    if o == "L":
        f = (f - 1) % 4
        continue
    dx, dy = DIRS[f]
    for _ in range(o):
        pl = x + dx, y + dy
        if pl not in g:
            dim, fn = WRAPS[f]
            lpl = list(pl)
            lpl[not dim] = fn(e[not dim] for e in g if e[dim] == pl[dim])
            pl = tuple(lpl)
        if g[pl]:
            break
        x, y = pl
sm((1000 * (y + 1)) + (4 * (x + 1)) + f)


# part 2
RNGS = [
    lambda _, mxx, mny, mxy, d: [(mxx - 1 + d, y) for y in range(mny, mxy)],
    lambda mnx, mxx, _, mxy, d: [(x, mxy - 1 + d) for x in range(mxx - 1, mnx - 1, -1)],
    lambda mnx, _, mny, mxy, d: [(mnx - d, y) for y in range(mxy - 1, mny - 1, -1)],
    lambda mnx, mxx, mny, _, d: [(x, mny - d) for x in range(mnx, mxx)],
]


class Side:
    def __init__(self, name, bounds):
        self.name = name
        self.bounds = bounds
        self.dirs = [None, None, None, None]


sds = []
mxx = max(e[0] for e in g) + 1
mxy = max(e[1] for e in g) + 1
for xd, yd in [(2, 5), (3, 4), (4, 3), (5, 2)]:
    sdln1, r1 = divmod(mxx, xd)
    sdln2, r2 = divmod(mxy, yd)
    if sdln1 == sdln2 and r1 == r2 == 0:
        sdln = sdln1
i = 1
for y in range(0, mxy, sdln):
    for x in range(0, mxx, sdln):
        if (x, y) not in g:
            continue
        sds.append(Side(i, (x, x + sdln, y, y + sdln)))
        i += 1
for sd in sds:
    mnx, mxx, mny, mxy = sd.bounds
    for osd in sds:
        if osd is sd:
            continue
        omnx, omxx, omny, omxy = osd.bounds
        if (mxx, mny) == (omnx, omny):
            sd.dirs[0] = osd, 2
            continue
        if (mnx, mxy) == (omnx, omny):
            sd.dirs[1] = osd, 3
            continue
        if (mnx, mny) == (omxx, omny):
            sd.dirs[2] = osd, 0
            continue
        if (mnx, mny) == (omnx, omxy):
            sd.dirs[3] = osd, 1
            continue
while True:
    changed = False
    for sd in sds:
        for t2r, frsd in enumerate(sd.dirs):
            t2l = (t2r + 1) % 4
            flsd = sd.dirs[t2l]
            if frsd is None or flsd is None:
                continue
            rsd, r2t = frsd
            lsd, l2t = flsd
            r2l = (r2t - 1) % 4
            l2r = (l2t + 1) % 4
            fr2l = lsd, l2r
            fl2r = rsd, r2l
            if rsd.dirs[r2l] is not None:
                continue
            rsd.dirs[r2l] = fr2l
            lsd.dirs[l2r] = fl2r
            changed = True
    if not changed:
        break
rdrs = {}
for csd in sds:
    for c2n, (nsd, n2c) in enumerate(csd.dirs):
        ssq = [(*e, c2n) for e in RNGS[c2n](*csd.bounds, True)]
        esq = [(*e, (n2c + 2) % 4) for e in RNGS[n2c](*nsd.bounds, False)]
        esq.reverse()
        rdrs |= dict(zip(ssq, esq))

y = min(e[1] for e in g)
x = min(e[0] for e in g if e[1] == y and not g[e])
f = 0
for o in os:
    if o == "R":
        f = (f + 1) % 4
        continue
    if o == "L":
        f = (f - 1) % 4
        continue
    for _ in range(o):
        dx, dy = DIRS[f]
        pl = x + dx, y + dy, f
        if pl in rdrs:
            pl = rdrs[pl]
        px, py, _ = pl
        if g[(px, py)]:
            break
        x, y, f = pl
sm((1000 * (y + 1)) + (4 * (x + 1)) + f)
