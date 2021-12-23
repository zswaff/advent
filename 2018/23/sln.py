#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from search import *
from web import *


# part 1
ns = []
mrn = (0, -1)
for i, l in enumerate(ls):
    p, r = l[5:].split('>, r=')
    r = int(r)
    mrn = max(mrn, (r, i))
    ns.append((*(int(e) for e in p.split(',')), r))
mx, my, mz, mr = ns[mrn[1]]
sm(sum(abs(mx - x) + abs(my - y) + abs(mz - z) <= mr for x, y, z, _ in ns))


# part 2
class Region:
    def __init__(self, mnx, mny, mnz, mxx, mxy, mxz):
        self.mnx = mnx
        self.mny = mny
        self.mnz = mnz
        self.mxx = mxx
        self.mxy = mxy
        self.mxz = mxz
        self.one = mnx == mxx and mny == mxy and mnz == mxz

        self.cnt = 0
        for x, y, z, r in ns:
            dx = 0 if mnx <= x <= mxx else min(abs(mnx - x), abs(mxx - x))
            dy = 0 if mny <= y <= mxy else min(abs(mny - y), abs(mxy - y))
            dz = 0 if mnz <= z <= mxz else min(abs(mnz - z), abs(mxz - z))
            if dx + dy + dz <= r:
                self.cnt += 1

        cx = 0 if mnx <= 0 <= mxx else min(abs(mnx), abs(mxx))
        cy = 0 if mny <= 0 <= mxy else min(abs(mny), abs(mxy))
        cz = 0 if mnz <= 0 <= mxz else min(abs(mnz), abs(mxz))
        self.dist = cx + cy + cz

    def divide(self):
        if self.mnx == self.mxx:
            xs = [(self.mnx, self.mxx)]
        else:
            hx = (self.mxx - self.mnx) // 2 + self.mnx
            xs = [(self.mnx, hx), (hx + 1, self.mxx)]
        if self.mny == self.mxy:
            ys = [(self.mny, self.mxy)]
        else:
            hy = (self.mxy - self.mny) // 2 + self.mny
            ys = [(self.mny, hy), (hy + 1, self.mxy)]
        if self.mnz == self.mxz:
            zs = [(self.mnz, self.mxz)]
        else:
            hz = (self.mxz - self.mnz) // 2 + self.mnz
            zs = [(self.mnz, hz), (hz + 1, self.mxz)]
        return [
            Region(nmnx, nmny, nmnz, nmxx, nmxy, nmxz)
            for (nmnx, nmxx), (nmny, nmxy), (nmnz, nmxz)
            in product(xs, ys, zs)
        ]


sr = Region(
    min(e[0] - e[3] for e in ns),
    min(e[1] - e[3] for e in ns),
    min(e[2] - e[3] for e in ns),
    max(e[0] + e[3] for e in ns),
    max(e[1] + e[3] for e in ns),
    max(e[2] + e[3] for e in ns)
)
q = PQ()
q.push(sr, (-sr.cnt, sr.dist))
while q:
    nr = q.pop()[0]
    if nr.one:
        sm(nr.dist)
        break
    for nnr in nr.divide():
        q.push(nnr, (-nnr.cnt, nnr.dist))
