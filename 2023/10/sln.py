#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
F = {
    "|": {"N", "S"},
    "-": {"E", "W"},
    "L": {"N", "E"},
    "J": {"N", "W"},
    "7": {"S", "W"},
    "F": {"S", "E"},
}
D = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}
O = {
    "N": "S",
    "E": "W",
    "S": "N",
    "W": "E",
}
g = gr(ls)
s = next(k for k, v in g.items() if v == "S")
for d in ["N", "E", "S"]:
    c = s
    t = 0
    while True:
        dc = D[d]
        c = (c[0] + dc[0], c[1] + dc[1])
        t += 1
        n = g.get(c, ".")
        if n == "S":
            break
        o = O[d]
        x = F.get(n, set())
        if o not in x:
            t = None
            break
        d = next(e for e in x if e != o)
    if t is not None:
        sm(t // 2)
        break


# part 2
for sd in ["N", "E", "S"]:
    bounds = set()
    d = sd
    c = s
    t = 0
    while True:
        bounds.add(c)
        dc = D[d]
        bounds.add((c[0] + dc[0] / 2, c[1] + dc[1] / 2))
        c = (c[0] + dc[0], c[1] + dc[1])
        t += 1
        n = g.get(c, ".")
        if n == "S":
            break
        o = O[d]
        x = F.get(n, set())
        if o not in x:
            t = None
            break
        d = next(e for e in x if e != o)
    if t is not None:
        break
mx, my = max(e[0] for e in g), max(e[1] for e in g)


class State(BaseSearchState):
    def __init__(self, x, y, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.dist = dist

    def is_valid(self):
        return -0.5 <= self.x <= mx + 0.5 and -0.5 <= self.y <= my + 0.5

    def is_finished(self):
        return False

    def get_neighbors(self):
        return [
            State(self.x + dx / 2, self.y + dy / 2, self.dist + 1)
            for k, (dx, dy) in D.items()
            if (self.x + dx / 2, self.y + dy / 2) not in bounds
        ]

    def get_dist_from_start(self):
        return self.dist


out = {(e.x, e.y) for e in State(-0.5, -0.5, 0).search().visited}
inn = set(g.keys()) - bounds - out
sm(len(inn))
