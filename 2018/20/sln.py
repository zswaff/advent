#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from search import *
from web import *


DIRS = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}


g = defaultdict(set)
x = y = 0
s = []
for c in dt[1:-1]:
    if c in DIRS:
        dx, dy = DIRS[c]
        nx, ny = x + dx, y + dy
        g[(x, y)].add((nx, ny))
        g[(nx, ny)].add((x, y))
        x, y = nx, ny
        continue
    if c == "(":
        s.append((x, y))
        continue
    if c == "|":
        x, y = s[-1]
        continue
    if c == ")":
        x, y = s.pop()
        continue
    print(c)

mx = 0
far = set()


class State(BaseSearchState):
    def __init__(self, loc, dist):
        super().__init__()
        self.loc = loc
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return False

    def get_neighbors(self):
        return [State(e, self.dist + 1) for e in g[self.loc]]

    def get_dist_from_start(self):
        return self.dist

    def process(self):
        global mx
        mx = max(mx, self.dist)
        if self.dist >= 1000:
            far.add(self.loc)


State((0, 0), 0).search()


# part 1
sm(mx)


# part 2
sm(len(far))
