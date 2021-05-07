#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from search import BaseSearchState


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
g = {}
for line in lines:
    k, v = line.split(' <-> ')
    g[k] = v.split(', ')


# part 1
class State(BaseSearchState):
    def __init__(self, name, dist):
        super().__init__()
        self.name = name
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return False

    def get_neighbors(self):
        return [State(e, self.dist + 1) for e in g[self.name]]

    def get_dist_from_start(self):
        return self.dist

print(len(State('0', 0).search().visited))


# part 2
count = 0
grouped = set()
for prog in g.keys():
    if prog in grouped:
        continue
    grouped |= {e.name for e in State(prog, 0).search().visited}
    count += 1
print(count)
