#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import combinations

from util import PQ


class State:
    def __init__(self, elvl, lvls, dist):
        self.elvl = elvl
        self.lvls = lvls
        self.dist = dist

    def __hash__(self):
        return hash((
            self.elvl,
            tuple(tuple(sorted(v)) for _, v in sorted(self.lvls.items()))
        ))

    def __eq__(self, other):
        return self.elvl == other.elvl and self.lvls == other.lvls

    def __repr__(self):
        return f'<E:{self.elvl} LS:{self.lvls} D:{self.dist}>'

    def is_valid(self):
        for lvl in self.lvls.values():
            ls = {e for e in lvl if e.islower()}
            us = {e.lower() for e in lvl if e.isupper()}
            if us and ls - us:
                return False
        return 1 <= self.elvl <= 4

    def is_finished(self):
        return all(k == 4 or not v for k, v in self.lvls.items())

    def get_nbors(self):
        res = []
        for delvl in [-1, 1]:
            nelvl = self.elvl + delvl
            if not 1 <= nelvl <= 4:
                continue
            lvl = self.lvls[self.elvl]
            ps = list(lvl) + list(combinations(lvl, 2))
            for p in ps:
                nlvls = {k: set(v) for k, v in self.lvls.items()}
                sp = set(p)
                nlvls[self.elvl] -= sp
                nlvls[nelvl] |= sp
                s = State(nelvl, nlvls, self.dist + 1)
                if s.is_valid():
                    res.append(s)
        return res

    def get_min_dist(self):
        return sum((4 - k) * len(v) for k, v in self.lvls.items())

    def get_dist_to_finish(self):
        q = PQ()
        q.push(self, self.dist)
        vis = set()
        while q:
            curr, _ = q.pop()
            if curr.is_finished():
                return curr.dist
            if curr in vis:
                continue
            vis.add(curr)
            for nbor in curr.get_nbors():
                q.push(nbor, nbor.dist + nbor.get_min_dist())


# part 1
print(State(
    1,
    {
        1: {'T', 't'},
        2: {'B', 'U', 'R', 'L'},
        3: {'b', 'u', 'r', 'l'},
        4: set()
    },
    0
).get_dist_to_finish())


# part 2
print(State(
    1,
    {
        1: {'T', 't', 'E', 'e', 'D', 'd'},
        2: {'B', 'U', 'R', 'L'},
        3: {'b', 'u', 'r', 'l'},
        4: set()
    },
    0
).get_dist_to_finish())
