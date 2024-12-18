#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
DS = ((0, -1), (1, 0), (0, 1), (-1, 0))
S = 70

pls = pas("{i},{i}")

g = {(x, y): False for x in range(S + 1) for y in range(S + 1)}
for x, y in pls[:1024]:
    g[(x, y)] = True


class State(BaseSearchState):
    def __init__(self, x, y, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.dist = dist

    def is_valid(self):
        return not g.get(self.p, True)

    def is_finished(self):
        return self.p == (S, S)

    def get_neighbors(self):
        return [State(self.x + dx, self.y + dy, self.dist + 1) for dx, dy in DS]


sm(State(0, 0, 0).search().distance)


# part 2
for i in range(1024, len(pls)):
    g = {(x, y): False for x in range(S + 1) for y in range(S + 1)}
    for x, y in pls[:i]:
        g[(x, y)] = True
    if State(0, 0, 0).search().distance is None:
        break
sm(ls[i - 1])
