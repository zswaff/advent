#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
DS = {
    "U": (0, 1),
    "R": (1, 0),
    "D": (0, -1),
    "L": (-1, 0),
}

cx, cy = 0, 0
es = {(cx, cy)}
for l in ls:
    spl = l.split(" ")
    d, n = spl[0], int(spl[1])
    for _ in range(n):
        cx += DS[d][0]
        cy += DS[d][1]
        es.add((cx, cy))


class State(BaseSearchState):
    def __init__(self, x, y, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return False

    def get_neighbors(self):
        return [
            State(self.x + dx, self.y + dy, self.dist + 1)
            for dx, dy in DS.values()
            if (self.x + dx, self.y + dy) not in es
        ]

    def get_dist_from_start(self):
        return self.dist


sm(len(es) + len(State(1, 1, 0).search().visited))


# part 2
NS = "RDLU"


cx, cy = 0, 0
vs = [(cx, cy)]
for l in ls:
    h = l.split(" ")[-1][2:-1]
    d = NS[int(h[-1])]
    n = int(h[:-1], 16)
    cx, cy = cx + DS[d][0] * n, cy + DS[d][1] * n
    vs.append((cx, cy))

p = Polygon(vs)
nvs = []
for v in vs:
    ccrns = {
        (v[0] + 0.5, v[1] + 0.5),
        (v[0] + 0.5, v[1] - 0.5),
        (v[0] - 0.5, v[1] - 0.5),
        (v[0] - 0.5, v[1] + 0.5),
    }
    crns = {e for e in ccrns if p.contains(Point(e))}
    if len(crns) == 1:
        inp = list(crns)[0]
        nvs.append((v[0] * 2 - inp[0], v[1] * 2 - inp[1]))
    else:
        nvs.append(list(ccrns - crns)[0])

sm(int(Polygon(nvs).area))
