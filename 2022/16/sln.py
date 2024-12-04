#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
fs = {}
g = {}
for l in ls:
    s, f, _, _, d = pa("Valve {} has flow rate={i}; tunnel{} to valve{} {}", l)
    if f != 0:
        fs[s] = f
    g[s] = d.split(", ")

mx = 0


class State(BaseSearchState):
    def __init__(self, l, s, op, dist):
        super().__init__()
        self.l = l
        self.s = s
        self.op = op
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return self.dist == 30

    def get_neighbors(self):
        if len(self.op) == len(fs):
            return []
        if self.s + (sum(fs.values()) * (30 - self.dist - 1)) <= mx:
            return []
        res = [State(nl, self.s, self.op, self.dist + 1) for nl in g[self.l]]
        if self.l in fs and self.l not in self.op:
            nop = tuple(sorted(self.op + (self.l,)))
            res.append(
                State(
                    self.l,
                    self.s + (fs[self.l] * (30 - self.dist - 1)),
                    nop,
                    self.dist + 1,
                )
            )
        return res

    def get_dist_from_start(self):
        return self.dist

    def process(self):
        global mx
        mx = max(mx, self.s)


State("AA", 0, (), 0).search()
sm(mx)


# part 2
paths = []
ng = cngr({k: {e: 1 for e in v} for k, v in g.items()}, fs.keys())


class State2(BaseSearchState):
    def __init__(self, l, scores, dist):
        super().__init__()
        self.l = l
        self.scores = scores
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return False

    def get_neighbors(self):
        if self.dist >= 26:
            return []
        dsc = fs[self.l] * (26 - self.dist)
        oscores = {e[0] for e in self.scores}
        nscores = tuple(sorted(self.scores + ((self.l, dsc),)))
        res = []
        for nl, dd in ng[self.l].items():
            if nl in oscores:
                continue
            res.append(State2(nl, nscores, self.dist + dd + 1))
        if len(res) == 0:
            res.append(State2(self.l, nscores, 26))
        return res

    def get_dist_from_start(self):
        return self.dist

    def process(self):
        if self.dist < 26:
            return
        paths.append(self.scores)


for l, t in cngr({k: {e: 1 for e in v} for k, v in g.items()}, {"AA"} | set(fs.keys()))[
    "AA"
].items():
    State2(l, (), t + 1).search()

sps = defaultdict(int)
for path in paths:
    key = tuple(e[0] for e in path)
    sps[key] = max(sps[key], sum(e[1] for e in path))

tps = [(set(k), v) for k, v in sps.items()]
mx = 0
for s1, t1 in tps:
    for s2, t2 in tps:
        if s1 & s2:
            continue
        mx = max(mx, t1 + t2)
sm(mx)
