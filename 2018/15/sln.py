#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common import *
from search import BaseSearchState
from web import *

DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

tg = set()
cs = {}
for y, l in enumerate(ls):
    for x, e in enumerate(l):
        if e == "#":
            continue
        if e != ".":
            cs[y, x] = [e == "E", 200]
        tg.add((y, x))
g = {}
for y, x in tg:
    g[(y, x)] = [(d, y + dy, x + dx) for d, (dy, dx) in enumerate(DIRS) if (y + dy, x + dx) in tg]


def run(cs, atk):
    cs = {k: list(v) for k, v in cs.items()}
    est = sum(e[0] for e in cs.values())

    def search(cy, cx, ct):
        mnd = inf
        cands = []

        class State(BaseSearchState):
            def __init__(self, loc, o_type, o_dir, dist):
                super().__init__()
                self.loc = loc
                self.o_type = o_type
                self.o_dir = o_dir
                self.dist = dist

            def is_valid(self):
                return True

            def process(self):
                if self.loc in cs and cs[self.loc][0] != self.o_type:
                    nonlocal mnd
                    mnd = min(mnd, self.dist)
                    if self.o_dir is not None:
                        cands.append((self.dist, self.loc, self.o_dir))

            def is_finished(self):
                return self.dist > mnd

            def get_neighbors(self):
                return [
                    State(
                        (ny, nx),
                        self.o_type,
                        d if self.o_dir is None else self.o_dir,
                        self.dist + 1,
                    )
                    for d, ny, nx in g[self.loc]
                    if (ny, nx) not in cs or cs[(ny, nx)][0] != self.o_type
                ]

            def get_dist_from_start(self):
                return self.dist

        State((cy, cx), ct, None, 0).search()
        return None if not cands else sorted(cands)[0][2]

    for i in count():
        csl = sorted([*k, v] for k, v in cs.items())
        for cy, cx, (ct, chp) in csl:
            if chp <= 0:
                continue
            efin = sum(e[0] for e in cs.values())
            if efin in {0, len(cs)}:
                return i * sum(e[1] for e in cs.values()), est == efin

            res = search(cy, cx, ct)
            if res is not None:
                dy, dx = DIRS[res]
                nl = cy + dy, cx + dx
                if nl not in cs:
                    cs[nl] = cs.pop((cy, cx))
                    cy, cx = nl

            targ = next(
                iter(
                    sorted(
                        (cs[(cy + dy, cx + dx)][1], j, (cy + dy, cx + dx))
                        for j, (dy, dx) in enumerate(DIRS)
                        if (cy + dy, cx + dx) in cs and cs[(cy + dy, cx + dx)][0] != ct
                    )
                ),
                None,
            )
            if targ is not None:
                tl = targ[2]
                cs[tl][1] -= atk if ct else 3
                if cs[tl][1] <= 0:
                    cs.pop(tl)


# part 1
sm(run(cs, 3)[0])

# part 2
for atk in count(4):
    scr, won = run(cs, atk)
    if won:
        sm(scr)
        break
