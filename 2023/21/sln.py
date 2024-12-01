#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
DS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
g = gr(ls)
s = next(k for k, v in g.items() if v == "S")
g[s] = "."

c = 0


class State(BaseSearchState):
    def __init__(self, x, y, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.d = dist
        self.dist = dist

    def get_neighbors(self):
        if self.d == 64:
            return []
        return [
            State(self.x + dx, self.y + dy, self.dist + 1)
            for dx, dy in DS
            if g.get((self.x + dx, self.y + dy), "#") != "#"
        ]

    def process(self):
        global c
        if self.d == 64:
            c += 1


State(s[0], s[1], 0).search()
sm(c)


# part 2
sd = max(e[0] for e in g) + 1
hsd = sd // 2

q = [s]
res = []
for i in count(1):
    nq = set()
    for x, y in q:
        for dx, dy in DS:
            nx, ny = x + dx, y + dy
            if g[(nx % sd, ny % sd)] != "#":
                nq.add((nx, ny))
    q = nq
    if i % sd == hsd:
        res.append(len(q))
        if len(res) == 3:
            break

b0, a1, a2 = res
b1 = a1 - b0
b2 = a2 - a1
n = 26501365 // sd
sm(b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1))
