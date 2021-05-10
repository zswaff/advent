#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict

from search import BaseSearchState


with open('inp.txt') as fin:
    grid = {
        (x, y): c
        for y, e in enumerate(fin.readlines())
        for x, c in enumerate(e.strip())
    }
goals = {e for e in grid.values() if e.isnumeric()}
mxx, mxy = max(e[0] for e in grid.keys()), max(e[1] for e in grid.keys())

dists = defaultdict(dict)


class GridState(BaseSearchState):
    def __init__(self, x, y, ival, dist):
        super().__init__({'ival'})
        self.x = x
        self.y = y
        self.ival = ival
        self.dist = dist

    def is_valid(self):
        return 0 <= self.x <= mxx and 0 <= self.y <= mxy and grid[(self.x, self.y)] != '#'

    def is_finished(self):
        return set(dists[self.ival].keys()) == goals

    def get_neighbors(self):
        return [
            GridState(self.x + dx, self.y + dy, self.ival, self.dist + 1)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ]

    def process(self):
        val = grid[(self.x, self.y)]
        if not val.isnumeric():
            return
        dists[self.ival][val] = self.dist

    def get_dist_from_start(self):
        return self.dist

for (x, y), v in grid.items():
    if v.isnumeric():
        GridState(x, y, v, 0).search()


# part 1
class State(BaseSearchState):
    def __init__(self, loc, visited, dist):
        super().__init__()
        self.loc = loc
        self.visited = visited
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return self.visited == goals

    def get_neighbors(self):
        return [
            State(nloc, frozenset(self.visited | {nloc}), self.dist + ddist)
            for nloc, ddist in dists[self.loc].items()
            if nloc != self.loc
        ]

    def get_dist_from_start(self):
        return self.dist

print(State('0', frozenset({'0'}), 0).search().result)


# part 2
class State(BaseSearchState):
    def __init__(self, loc, visited, dist):
        super().__init__()
        self.loc = loc
        self.visited = visited
        self.returned = len(self.visited) > 1 and loc == '0'
        self.dist = dist

    def is_valid(self):
        return not (self.returned and self.visited != goals)

    def is_finished(self):
        return self.visited == goals and self.returned

    def get_neighbors(self):
        return [
            State(nloc, frozenset(self.visited | {nloc}), self.dist + ddist)
            for nloc, ddist in dists[self.loc].items()
            if nloc != self.loc
        ]

    def get_dist_from_start(self):
        return self.dist

print(State('0', frozenset({'0'}), 0).search().result)
