#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


rawbs = [
    pa(
        "Blueprint {i}: Each ore robot costs {i} ore. Each clay robot costs {i} ore. Each obsidian robot costs {i} ore and {i} clay. Each geode robot costs {i} ore and {i} obsidian.",
        l,
    )
    for l in ls
]
bs = [
    (a, ((b, 0, 0, 0), (c, 0, 0, 0), (d, e, 0, 0), (f, 0, g, 0)))
    for a, b, c, d, e, f, g in rawbs
]


def calc(cs, rnds):
    mx = 0
    mxrbs = tuple(max(e) for e in zip(*cs))[:3] + (inf,)

    class State(BaseSearchState):
        def __init__(self, rss, rbs, als, dist):
            super().__init__()
            self.rss = rss
            self.rbs = rbs
            self.als = als
            self.dist = dist

        def is_valid(self):
            rem = rnds - self.dist
            mxp = self.rss[3] + ((rem * (rem + 1)) // 2)
            nonlocal mx
            return (
                self.dist <= rnds
                and mxp > mx
                and all(e <= f for e, f in zip(self.rbs, mxrbs))
            )

        def is_finished(self):
            return False

        def get_neighbors(self):
            ndist = self.dist + 1
            nrss = tuple(e + f for e, f in zip(self.rss, self.rbs))
            if all(e >= f for e, f in zip(self.rss, cs[3])):
                return [
                    State(
                        tuple(e - f for e, f in zip(nrss, cs[3])),
                        tuple(e + (j == 3) for j, e in enumerate(self.rbs)),
                        (True, True, True, True),
                        ndist,
                    )
                ]
            res = []
            nals = []
            for i, (al, c) in enumerate(zip(self.als, cs)):
                if not al:
                    nals.append(False)
                    continue
                if any(e < f for e, f in zip(self.rss, c)):
                    nals.append(True)
                    continue
                nals.append(False)
                res.append(
                    State(
                        tuple(e - f for e, f in zip(nrss, c)),
                        tuple(e + (j == i) for j, e in enumerate(self.rbs)),
                        (True, True, True, True),
                        ndist,
                    )
                )
            if any(nals):
                res.append(State(nrss, self.rbs, tuple(nals), ndist))
            return res

        def process(self):
            nonlocal mx
            mx = max(mx, self.rss[3])

    State((0, 0, 0, 0), (1, 0, 0, 0), (True, True, True, True), 0).search()
    return mx


# part 1
sm(sum(i * calc(e, 24) for i, e in bs))


# part 2
sm(prod(calc(e[1], 32) for e in bs[:3]))
