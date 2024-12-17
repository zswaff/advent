#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
DS = ((0, -1), (1, 0), (0, 1), (-1, 0))

g = gr()
st = next(k for k, v in g.items() if v == "S")
en = next(k for k, v in g.items() if v == "E")
g = {k for k, v in g.items() if v == "#"}


class State(BaseSearchState):
    def __init__(self, x, y, o, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.o = o
        self.dist = dist

    def is_valid(self):
        return self.p not in g

    def is_finished(self):
        return self.p == en

    def get_neighbors(self):
        dx, dy = DS[self.o]
        return [
            State(self.x + dx, self.y + dy, self.o, self.dist + 1),
            State(self.x, self.y, (self.o + 1) % 4, self.dist + 1000),
            State(self.x, self.y, (self.o - 1) % 4, self.dist + 1000),
        ]


r1 = State(st[0], st[1], 1, 0).search().distance
sm(r1)


# part 2
r2 = {}


class State(BaseSearchState):
    def __init__(self, x, y, o, prev, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.o = o
        self.prev = prev
        self.dist = dist

    def is_valid(self):
        f = self.p, self.o
        return self.p not in g and (f not in r2 or self.dist == r2[f][0])

    def get_neighbors(self):
        dx, dy = DS[self.o]
        prev = self.p, self.o
        return [
            State(self.x + dx, self.y + dy, self.o, prev, self.dist + 1),
            State(self.x, self.y, (self.o + 1) % 4, prev, self.dist + 1000),
            State(self.x, self.y, (self.o - 1) % 4, prev, self.dist + 1000),
        ]

    def process(self):
        f = self.p, self.o
        global r2
        if f not in r2:
            r2[f] = self.dist, []
        if self.prev is None:
            return
        r2[f][1].append(self.prev)


State(st[0], st[1], 1, None, 0).search()

q = [(en, e) for e in range(4) if (en, e) in r2]
vis = set()
while q:
    n = q.pop()
    if n in vis:
        continue
    vis.add(n)
    for p in r2[n][1]:
        q.append(p)
sm(len({e[0] for e in vis}))
