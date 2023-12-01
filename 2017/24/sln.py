#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from search import BaseSearchState


with open("inp.txt") as fin:
    comps = {tuple(int(f) for f in e.strip().split("/")) for e in fin.readlines()}


# part 1
mx = 0


class State(BaseSearchState):
    def __init__(self, last, tot, visited):
        super().__init__()
        self.last = last
        self.tot = tot
        self.visited = visited

    def is_valid(self):
        return True

    def is_finished(self):
        return False

    def get_neighbors(self):
        res = []
        for n in comps - set(self.visited):
            a, b = n
            if a == self.last:
                res.append(State(b, self.tot + a + b, tuple(sorted(self.visited + (n,)))))
                continue
            if b == self.last:
                res.append(State(a, self.tot + a + b, tuple(sorted(self.visited + (n,)))))
        return res

    def get_dist_from_start(self):
        return 0

    def process(self):
        global mx
        mx = max(mx, self.tot)


State(0, 0, ()).search()
print(mx)


# part 2
mx = 0, 0


class State(BaseSearchState):
    def __init__(self, length, last, tot, visited):
        super().__init__()
        self.length = length
        self.last = last
        self.tot = tot
        self.visited = visited

    def is_valid(self):
        return True

    def is_finished(self):
        return False

    def get_neighbors(self):
        res = []
        for n in comps - set(self.visited):
            a, b = n
            if a == self.last:
                res.append(
                    State(self.length + 1, b, self.tot + a + b, tuple(sorted(self.visited + (n,))))
                )
                continue
            if b == self.last:
                res.append(
                    State(self.length + 1, a, self.tot + a + b, tuple(sorted(self.visited + (n,))))
                )
        return res

    def get_dist_from_start(self):
        return 0

    def process(self):
        global mx
        mx = max(mx, (self.length, self.tot))


State(0, 0, 0, ()).search()
print(mx[1])
