#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import lru_cache
from collections import Counter

from util import BaseSearchState


INP = 1352


@lru_cache
def is_open(x, y):
    return Counter(bin(x*x + 3*x + 2*x*y + y + y*y + INP)[2:])['1'] % 2 == 0


class State(BaseSearchState):
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def is_valid(self):
        return self.x >= 0 and self.y >= 0 and is_open(self.x, self.y)

    def is_finished(self):
        return (self.x, self.y) == (31, 39)

    def get_neighbors(self):
        return [
            State(self.x + dx, self.y + dy, self.dist + 1)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ]

    def get_dist_from_start(self):
        return self.dist


# part 1
print(State(1, 1, 0).search())


# part 2
q = [State(1, 1, 0)]
vis = set()
while q:
    curr = q.pop(0)
    if not curr.is_valid():
        continue
    if curr.dist > 50:
        break
    if curr in vis:
        continue
    vis.add(curr)
    for nbor in curr.get_neighbors():
        q.append(nbor)
print(len(vis))
