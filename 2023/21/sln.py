#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


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
