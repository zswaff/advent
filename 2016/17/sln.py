#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from hashlib import md5

from search import BaseSearchState


INP = 'udskfozm'


DIRS = [('U', 0, -1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0)]


class State(BaseSearchState):
    def __init__(self, x, y, path, dist):
        super().__init__()
        self.x = x
        self.y = y
        self.path = path
        self.dist = dist

    def is_valid(self):
        return 0 <= self.x <= 3 and 0 <= self.y <= 3

    def is_finished(self):
        return (self.x, self.y) == (3, 3)

    def get_neighbors(self):
        hsh = md5((INP + self.path).encode()).hexdigest()[:4]
        return [
            State(self.x + dx, self.y + dy, self.path + dp, self.dist + 1)
            for c, (dp, dx, dy) in zip(hsh, DIRS)
            if int(c, 16) > 10
        ]

    def get_dist_from_start(self):
        return self.dist


# part 1
def bfs(self):
    q = [self]
    vis = set()
    while q:
        curr = q.pop(0)
        if not curr.is_valid():
            continue
        if curr in vis:
            continue
        vis.add(curr)
        if curr.is_finished():
            return curr.path
        for nbor in curr.get_neighbors():
            q.append(nbor)
print(bfs(State(0, 0, '', 0)))


# part 2
def bfs(self):
    m = 0
    q = [self]
    vis = set()
    while q:
        curr = q.pop(0)
        if not curr.is_valid():
            continue
        if curr in vis:
            continue
        vis.add(curr)
        if curr.is_finished():
            m = max(m, curr.dist)
            continue
        for nbor in curr.get_neighbors():
            q.append(nbor)
    return m
print(bfs(State(0, 0, '', 0)))
