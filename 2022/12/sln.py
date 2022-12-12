#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

g = gr(ls, ord)
s = next(k for k, v in g.items() if v == ord("S"))
g[s] = ord("a")
e = next(k for k, v in g.items() if v == ord("E"))
g[e] = ord("z")


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
        return (self.x, self.y) == e

    def get_neighbors(self):
        mx = g[(self.x, self.y)] + 1
        return [
            State(self.x + dx, self.y + dy, self.dist + 1)
            for dx, dy in DIRS
            if g.get((self.x + dx, self.y + dy), inf) <= mx
        ]

    def get_dist_from_start(self):
        return self.dist


sm(State(*s, 0).search().distance)


# part 2
class State2(BaseSearchState):
    def __init__(self, x, y, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return g[(self.x, self.y)] == ord("a")

    def get_neighbors(self):
        mn = g[(self.x, self.y)] - 1
        return [
            State2(self.x + dx, self.y + dy, self.dist + 1)
            for dx, dy in DIRS
            if g.get((self.x + dx, self.y + dy), -inf) >= mn
        ]

    def get_dist_from_start(self):
        return self.dist


sm(State2(*e, 0).search().distance)
