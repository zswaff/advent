#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from search import *
from web import *


g = {(x, y): int(e) for y, l in enumerate(ls) for x, e in enumerate(l)}
mxx, mxy = max(e[0] for e in g.keys()), max(e[1] for e in g.keys())


# part 1
class State(BaseSearchState):
    def __init__(self, x, y, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return self.x == mxx and self.y == mxy

    def get_neighbors(self):
        return [
            State(self.x + dx, self.y + dy, self.dist + g[(self.x + dx, self.y + dy)])
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if (self.x + dx, self.y + dy) in g
        ]

    def get_dist_from_start(self):
        return self.dist


sm(State(0, 0, 0).search().distance)


# part 2
nmxx, nmxy = mxx * 5 + 4, mxy * 5 + 4
ng = {}
for fx in range(5):
    for fy in range(5):
        p = fx + fy
        for (x, y), e in g.items():
            ng[(x + (mxx + 1) * fx, y + (mxy + 1) * fy)] = (e + p - 1) % 9 + 1


class State(BaseSearchState):
    def __init__(self, x, y, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return self.x == nmxx and self.y == nmxy

    def get_neighbors(self):
        return [
            State(self.x + dx, self.y + dy, self.dist + ng[(self.x + dx, self.y + dy)])
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if (self.x + dx, self.y + dy) in ng
        ]

    def get_dist_from_start(self):
        return self.dist

    def get_dist_to_finish_heuristic(self):
        return abs(self.x - nmxx) + abs(self.y - nmxy)


sm(State(0, 0, 0).search().distance)
