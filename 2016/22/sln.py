#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from util import BaseSearchState


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
ns = {}
for line in lines[2:]:
    splt = line.split()
    locstrs = splt[0].split('/')[-1].split('-')[1:]
    loc = int(locstrs[0][1:]), int(locstrs[1][1:])
    ns[loc] = [int(e[:-1]) for e in splt[1:]]
mnx, mxx = min(e[0] for e in ns.keys()), max(e[0] for e in ns.keys())
mny, mxy = min(e[1] for e in ns.keys()), max(e[1] for e in ns.keys())

c = 0
for loca, (_, useda, _, _) in ns.items():
    if useda == 0:
        continue
    for locb, (_, _, availb, _) in ns.items():
        if loca == locb:
            continue
        if useda <= availb:
            c += 1
print(c)


# part 2
class State(BaseSearchState):
    def __init__(self, goal, ntwk, dist):
        self.goal = goal
        self.ntwk = ntwk
        self.dist = dist

    def __hash__(self):
        return hash((self.goal, tuple(sorted(self.ntwk.items()))))

    def __eq__(self, other):
        return self.goal == other.goal and self.ntwk == other.ntwk

    def __repr__(self):
        return f'<d={self.dist} g={self.goal} n={self.ntwk}>'

    def is_valid(self):
        return True

    def is_finished(self):
        return self.goal == (0, 0)

    def get_neighbors(self):
        r = []
        for (x, y), used in self.ntwk.items():
            loc = x, y
            for dx, dy in DIRS:
                nloc = x + dx, y + dy
                if nloc not in self.ntwk:
                    continue
                nused = self.ntwk[nloc]
                if used + nused > ns[nloc][0]:
                    continue
                nntwk = dict(self.ntwk)
                nntwk[loc] = 0
                nntwk[nloc] = nused + used
                ngoal = nloc if self.goal == loc else self.goal
                r.append(State(ngoal, nntwk, self.dist + 1))
        return r

    def get_dist_from_start(self):
        return self.dist

    def get_dist_to_finish_heuristic(self):
        return self.goal[0] + self.goal[1]


print(State((mxx, 0), {k: v[1] for k, v in ns.items()}, 0).a_star())
