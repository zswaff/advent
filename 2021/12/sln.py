#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from search import *
from web import *


g = defaultdict(set)
for l in ls:
    e, f = l.split('-')
    g[e].add(f)
    g[f].add(e)


# part 1
class State(BaseSearchState):
    def __init__(self, loc, visited):
        super().__init__()
        self.loc = loc
        self.visited = visited

    def is_valid(self):
        return True

    def is_finished(self):
        return False

    def get_neighbors(self):
        if self.loc == 'end':
            return []
        v = self.visited + (self.loc,)
        return [State(e, v) for e in g[self.loc] if e == e.upper() or e not in v]

    def get_dist_from_start(self):
        return 0

    def process(self):
        if self.loc != 'end':
            return
        global c
        c += 1


c = 0
State('start', ()).search()
sm(c)


# part 2
class State(BaseSearchState):
    def __init__(self, loc, visited):
        super().__init__()
        self.loc = loc
        self.visited = visited

    def is_valid(self):
        return True

    def is_finished(self):
        return False

    def get_neighbors(self):
        if self.loc == 'end':
            return []
        v = self.visited + (self.loc,)
        sv = set(v)
        p = Counter([e for e in v if e == e.lower()]).most_common()[0][1] == 1
        return [State(e, v) for e in g[self.loc] if (e == e.upper() or e not in sv or p) and e != 'start']

    def get_dist_from_start(self):
        return 0

    def process(self):
        if self.loc != 'end':
            return
        global c
        c += 1


c = 0
State('start', ()).search()
sm(c)
