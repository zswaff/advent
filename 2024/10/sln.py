#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
g = gr(ls, lambda x: int(x) if x != "." else -1)
c = 0


class State(BaseSearchState):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def get_neighbors(self):
        return [
            State(self.x + dx, self.y + dy)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
            if g.get((self.x + dx, self.y + dy)) == g[self.p] + 1
        ]

    def process(self):
        global c
        if g[self.p] != 9:
            return
        c += 1


for (x, y), v in g.items():
    if v != 0:
        continue
    State(x, y).search()
sm(c)


# part 2
c = 0
w = None


class State(BaseSearchState):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def get_neighbors(self):
        res = [
            State(self.x + dx, self.y + dy)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
            if g.get((self.x + dx, self.y + dy)) == g[self.p] + 1
        ]
        for n in res:
            w[n.x, n.y] += w[self.p]
        return res

    def process(self):
        global c
        if g[self.p] != 9:
            return
        c += w[self.p]

    def get_dist_from_start(self):
        return g[self.p]


for (x, y), v in g.items():
    if v != 0:
        continue
    w = defaultdict(int)
    w[x, y] = 1
    State(x, y).search()
sm(c)
