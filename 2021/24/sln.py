#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


zds = [int(ls[i].split()[-1]) for i in range(4, len(ls), 18)]
xas = [int(ls[i].split()[-1]) for i in range(5, len(ls), 18)]
yas = [int(ls[i].split()[-1]) for i in range(15, len(ls), 18)]


# part 1
class State(BaseSearchState):
    def __init__(self, z, lv, dist):
        super().__init__()
        self.z = z
        self.lv = lv
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return self.lv == 14 and self.z == 0

    def get_neighbors(self):
        if self.lv == 14:
            return []
        r = []
        for w in range(9, 0, -1):
            x = int(w != ((self.z % 26) + xas[self.lv]))
            nz = ((self.z // zds[self.lv]) * ((25 * x) + 1)) + ((w + yas[self.lv]) * x)
            r.append(State(nz, self.lv + 1, self.dist - (w * (10 ** (13 - self.lv)))))
        return r

    def get_dist_from_start(self):
        return self.dist


sm(-State(0, 0, 0).search().distance)


# part 2
class State(BaseSearchState):
    def __init__(self, z, lv, dist):
        super().__init__()
        self.z = z
        self.lv = lv
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return self.lv == 14 and self.z == 0

    def get_neighbors(self):
        if self.lv == 14:
            return []
        r = []
        for w in range(1, 10):
            x = int(w != ((self.z % 26) + xas[self.lv]))
            nz = ((self.z // zds[self.lv]) * ((25 * x) + 1)) + ((w + yas[self.lv]) * x)
            r.append(State(nz, self.lv + 1, self.dist + (w * (10 ** (13 - self.lv)))))
        return r

    def get_dist_from_start(self):
        return self.dist


sm(State(0, 0, 0).search().distance)
