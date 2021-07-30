#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from search import *
from web import *


dpth, trg = ls
dpth = int(dpth.split(' ')[1])
tx, ty = (int(e) for e in trg.split(' ')[1].split(','))


g = {(0, 0): 0, (tx, ty): 0}
t = {}

def gnt(x, y):
    l = x, y
    if l in t:
        return g[l], t[l]
    if l not in g:
        if y == 0:
            gi = x * 16807
        elif x == 0:
            gi = y * 48271
        else:
            gi = gnt(x - 1, y)[0] * gnt(x, y - 1)[0]
        g[l] = (gi + dpth) % 20183
    t[l] = g[l] % 3
    return g[l], t[l]


# part 1
for x in range(0, tx + 1):
    for y in range(0, ty + 1):
        gnt(x, y)
sm(sum(t.values()))


# part 2
DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))
VALID_EQUIP = {'n': {1, 2}, 't': {0, 2}, 'c': {0, 1}}

class State(BaseSearchState):
    def __init__(self, x, y, equip, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.equip = equip
        self.dist = dist

    def is_valid(self):
        return self.x >= 0 and self.y >= 0 and \
               gnt(self.x, self.y)[1] in VALID_EQUIP[self.equip]

    def is_finished(self):
        return self.x == tx and self.y == ty and self.equip == 't'

    def get_neighbors(self):
        return [
            State(self.x + dx, self.y + dy, self.equip, self.dist + 1)
            for dx, dy in DIRS
        ] + [
            State(self.x, self.y, e, self.dist + 7)
            for e in VALID_EQUIP.keys() if e != self.equip
        ]

    def get_dist_from_start(self):
        return self.dist

    def get_dist_to_finish_heuristic(self):
        return abs(tx - self.x) + abs(ty - self.y)

sm(State(0, 0, 't', 0).search().distance)
