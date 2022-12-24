#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


DIRS = OrderedDict([(">", (1, 0)), ("v", (0, 1)), ("<", (-1, 0)), ("^", (0, -1))])


# part 1
g = {k: [] if v == "." else [v] for k, v in gr(ls).items() if v != "#"}
start = min(e for e in g.keys())
end = max((e for e in g.keys()), key=lambda e: e[1])
mnx, mxx = min(e[0] for e in g), max(e[0] for e in g)
mny, mxy = min(e[1] for e in g) + 1, max(e[1] for e in g) - 1

_gsc = [g]


def gs(idx):
    while idx >= len(_gsc):
        ng = {k: [] for k in _gsc[-1].keys()}
        for (x, y), vs in _gsc[-1].items():
            for v in vs:
                dx, dy = DIRS[v]
                nx = x + dx
                if nx < mnx:
                    nx = mxx
                if nx > mxx:
                    nx = mnx
                ny = y + dy
                if ny < mny:
                    ny = mxy
                if ny > mxy:
                    ny = mny
                ng[(nx, ny)].append(v)
        _gsc.append(ng)
    return _gsc[idx]


class State(BaseSearchState):
    def __init__(self, x, y, d):
        super().__init__()
        self.x = x
        self.y = y
        self.d = d

    def is_valid(self):
        return len(gs(self.d).get((self.x, self.y), [None])) == 0

    def is_finished(self):
        return (self.x, self.y) == end

    def get_neighbors(self):
        nd = self.d + 1
        return [State(self.x, self.y, nd)] + [
            State(self.x + dx, self.y + dy, nd) for dx, dy in DIRS.values()
        ]

    def get_dist_from_start(self):
        return self.d


sm(State(*start, 0).search().distance)


# part 2
class State2(BaseSearchState):
    def __init__(self, x, y, s, d):
        super().__init__()
        self.x = x
        self.y = y
        self.s = s
        self.d = d

    def is_valid(self):
        return len(gs(self.d).get((self.x, self.y), [None])) == 0

    def is_finished(self):
        return self.s == 3

    def get_neighbors(self):
        nd = self.d + 1
        res = [State2(self.x, self.y, self.s, nd)]
        for dx, dy in DIRS.values():
            nl = self.x + dx, self.y + dy
            ns = self.s
            if nl == end and self.s % 2 == 0:
                ns += 1
            if nl == start and self.s % 2 == 1:
                ns += 1
            res.append(State2(*nl, ns, nd))
        return res

    def get_dist_from_start(self):
        return self.d


sm(State2(*start, 0, 0).search().distance)
