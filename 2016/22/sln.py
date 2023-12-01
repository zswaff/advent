#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from search import BaseSearchState


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
ns = {}
for line in lines[2:]:
    splt = line.split()
    locstrs = splt[0].split("/")[-1].split("-")[1:]
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
mover = next(k for k, v in ns.items() if v[1] == 0)
bigs = {k for k, v in ns.items() if v[1] > ns[mover][0]}


class State(BaseSearchState):
    def __init__(self, empty, goal, dist):
        super().__init__()
        self.empty = empty
        self.goal = goal
        self.dist = dist

    def is_valid(self):
        return self.empty not in bigs

    def is_finished(self):
        return self.goal == (0, 0)

    def get_neighbors(self):
        r = []
        for dx, dy in DIRS:
            nempty = self.empty[0] + dx, self.empty[1] + dy
            if nempty not in ns:
                continue
            ngoal = self.empty if nempty == self.goal else self.goal
            r.append(State(nempty, ngoal, self.dist + 1))
        return r

    def get_dist_from_start(self):
        return self.dist

    def get_dist_to_finish_heuristic(self):
        return 0


print(State(mover, (mxx, 0), 0).search().result)
