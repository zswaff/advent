#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from search import BaseSearchState
from web import *


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

g = {(x, y): int(e) for y, l in enumerate(ls) for x, e in enumerate(l)}


# part 1
sm(sum(1 + e for (x, y), e in g.items() if all(e < g.get((x + dx, y + dy), inf) for dx, dy in DIRS)))


# part 2
c = Counter()


class State(BaseSearchState):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def is_valid(self):
        return True

    def is_finished(self):
        return all(g[(self.x, self.y)] < g.get((self.x + dx, self.y + dy), inf) for dx, dy in DIRS)

    def get_neighbors(self):
        return [
            State(self.x + dx, self.y + dy)
            for dx, dy in DIRS
            if g.get((self.x + dx, self.y + dy), inf) < g[(self.x, self.y)]
        ]

    def get_dist_from_start(self):
        return 0


for (x, y), e in g.items():
    if e == 9:
        continue
    end = State(x, y).search().end_state
    c[(end.x, end.y)] += 1
sm(prod(e[1] for e in c.most_common(3)))
