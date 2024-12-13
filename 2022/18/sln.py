#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def sz(cld):
    c = len(cld) * 6
    for x, y, z in cld:
        for dx, dy, dz in DIRS:
            if (x + dx, y + dy, z + dz) not in cld:
                continue
            c -= 1
    return c


ds = {tuple(pa("{i},{i},{i}", l)) for l in ls}


# part 1
sm(sz(ds))


# part 2
mnx, mxx = min(e for e, _, _ in ds) - 1, max(e for e, _, _ in ds) + 1
mny, mxy = min(e for _, e, _ in ds) - 1, max(e for _, e, _ in ds) + 1
mnz, mxz = min(e for _, _, e in ds) - 1, max(e for _, _, e in ds) + 1

os = set()


class State(BaseSearchState):
    def __init__(self, x, y, z, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.dist = dist

    def is_valid(self):
        return (
            (self.x, self.y, self.z) not in ds
            and mnx <= self.x <= mxx
            and mny <= self.y <= mxy
            and mnz <= self.z <= mxz
        )

    def get_neighbors(self):
        return [State(self.x + dx, self.y + dy, self.z + dz, 0) for dx, dy, dz in DIRS]

    def process(self):
        os.add((self.x, self.y, self.z))


State(mnx, mny, mnz, 0).search()
xs, ys, zs = mxx - mnx + 1, mxy - mny + 1, mxz - mnz + 1
sm(sz(os) - 2 * ((xs * ys) + (xs * zs) + (ys * zs)))
