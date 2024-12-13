#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
DS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}
TS = {
    "N": "EW",
    "E": "NS",
    "S": "EW",
    "W": "NS",
}


g = gr(ls, int)
mx = max(e[0] for e in g)
my = max(e[1] for e in g)


class State(BaseSearchState):
    def __init__(self, x, y, d, s, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.d = d
        self.s = s
        self.dist = dist

    def is_finished(self):
        return self.x == mx and self.y == my

    def get_neighbors(self):
        res = []
        for nd in TS[self.d]:
            nx, ny = self.x + DS[nd][0], self.y + DS[nd][1]
            if (nx, ny) not in g:
                continue
            res.append(State(nx, ny, nd, 0, self.dist + g[(nx, ny)]))
        if self.s < 2:
            nx, ny = self.x + DS[self.d][0], self.y + DS[self.d][1]
            if (nx, ny) in g:
                res.append(State(nx, ny, self.d, self.s + 1, self.dist + g[(nx, ny)]))
        return res


sm(min(State(0, 0, e, 0, 0).search().distance for e in "ES"))


# part 2
class State(BaseSearchState):
    def __init__(self, x, y, d, s, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.d = d
        self.s = s
        self.dist = dist

    def is_finished(self):
        return self.x == mx and self.y == my

    def get_neighbors(self):
        res = []
        if self.s > 2:
            for nd in TS[self.d]:
                nx, ny = self.x + DS[nd][0], self.y + DS[nd][1]
                if (nx, ny) not in g:
                    continue
                res.append(State(nx, ny, nd, 0, self.dist + g[(nx, ny)]))
        if self.s < 9:
            nx, ny = self.x + DS[self.d][0], self.y + DS[self.d][1]
            if (nx, ny) in g:
                res.append(State(nx, ny, self.d, self.s + 1, self.dist + g[(nx, ny)]))
        return res


sm(min(State(0, 0, e, 0, 0).search().distance for e in "ES"))
