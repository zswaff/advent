#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
d = defaultdict(bool)
for l in ls:
    o, x1, x2, y1, y2, z1, z2 = pa(l, "{} x={i}..{i},y={i}..{i},z={i}..{i}")
    if x1 < -50 or x1 > 50:
        continue
    o = o == "on"
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                d[(x, y, z)] = o
sm(sum(d.values()))


# part 2
def rs(mn, mx, omn, omx):
    if min(mx, omx) < max(mn, omn):
        return [(mn, mx, True)]
    r = []
    if mn < omn:
        r.append((mn, omn - 1, True))
    r.append((max(mn, omn), min(mx, omx), False))
    if mx > omx:
        r.append((omx + 1, mx, True))
    return r


class R:
    def __init__(self, mnx, mxx, mny, mxy, mnz, mxz, p):
        self.mnx = mnx
        self.mxx = mxx
        self.mny = mny
        self.mxy = mxy
        self.mnz = mnz
        self.mxz = mxz
        self.p = p

    def sz(self):
        return (
            (self.mxx - self.mnx + 1)
            * (self.mxy - self.mny + 1)
            * (self.mxz - self.mnz + 1)
            * (1 if self.p else -1)
        )

    def intersection(self, new):
        if any(
            [
                min(self.mxx, new.mxx) < max(self.mnx, new.mnx),
                min(self.mxy, new.mxy) < max(self.mny, new.mny),
                min(self.mxz, new.mxz) < max(self.mnz, new.mnz),
            ]
        ):
            return []
        return [
            R(
                max(self.mnx, new.mnx),
                min(self.mxx, new.mxx),
                max(self.mny, new.mny),
                min(self.mxy, new.mxy),
                max(self.mnz, new.mnz),
                min(self.mxz, new.mxz),
                not self.p,
            )
        ]

    def contains(self, other):
        return all(
            [
                self.mnx <= other.mnx,
                self.mxx >= other.mxx,
                self.mny <= other.mny,
                self.mxy >= other.mxy,
                self.mnz <= other.mnz,
                self.mxz >= other.mxz,
            ]
        )

    def sub(self, other):
        r = []
        for x1, x2, xo in rs(self.mnx, self.mxx, other.mnx, other.mxx):
            for y1, y2, yo in rs(self.mny, self.mxy, other.mny, other.mxy):
                for z1, z2, zo in rs(self.mnz, self.mxz, other.mnz, other.mxz):
                    if any([xo, yo, zo]):
                        r.append(R(x1, x2, y1, y2, z1, z2, True))
        if not r:
            return []
        nr = [r[0]]
        for e in r[1:]:
            f = nr.pop()
            if all(
                [
                    f.mnx == e.mnx,
                    f.mxx == e.mxx,
                    f.mny == e.mny,
                    f.mxy == e.mxy,
                    min(f.mxz, e.mxz) + 1 == max(f.mnz, e.mnz),
                ]
            ):
                nr.append(
                    R(
                        f.mnx,
                        f.mxx,
                        f.mny,
                        f.mxy,
                        min(f.mnz, e.mnz),
                        max(f.mxz, e.mxz),
                        True,
                    )
                )
            else:
                nr.append(f)
                nr.append(e)
        r = nr
        nr = [r[0]]
        for e in r[1:]:
            f = nr.pop()
            if all(
                [
                    f.mnx == e.mnx,
                    f.mxx == e.mxx,
                    f.mnz == e.mnz,
                    f.mxz == e.mxz,
                    min(f.mxy, e.mxy) + 1 == max(f.mny, e.mny),
                ]
            ):
                nr.append(
                    R(
                        f.mnx,
                        f.mxx,
                        min(f.mny, e.mny),
                        max(f.mxy, e.mxy),
                        f.mnz,
                        f.mxz,
                        True,
                    )
                )
            else:
                nr.append(f)
                nr.append(e)
        r = nr
        return r


subs = []
t = []
for l in reversed(ls):
    o, x1, x2, y1, y2, z1, z2 = pa(l, "{} x={i}..{i},y={i}..{i},z={i}..{i}")
    nr = R(x1, x2, y1, y2, z1, z2, o)
    if o == "off":
        subs.append(nr)
        continue
    nrs = [nr]
    for e in subs:
        nnrs = []
        for f in nrs:
            nnrs += f.sub(e)
        nrs = nnrs
    t += nrs

d = []
for e in t:
    nd = [e]
    cont = False
    for f in d:
        if f.contains(e):
            cont = True
        nd += f.intersection(e)
    if cont:
        continue
    d += nd
sm(sum(e.sz() for e in d))
