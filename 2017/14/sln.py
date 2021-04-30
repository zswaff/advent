#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from operator import xor
from functools import reduce

from search import BaseSearchState


SZ = 256
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


INP = 'jzgqcdpd'


def knot_hash(s):
    lns = ([ord(e) for e in s] + [17, 31, 73, 47, 23]) * 64
    pos = 0
    l = list(range(SZ))
    for skip, ln in enumerate(lns):
        l = l[pos:] + l[:pos]
        l = l[:ln][::-1] + l[ln:]
        l = l[-pos:] + l[:-pos]
        pos = (pos + ln + skip) % SZ
    return ''.join(
        f'{e:0>2x}'
        for e in [reduce(xor, l[i * 16:(i + 1) * 16]) for i in range(16)]
    )

def bin_knot_hash(s):
    return bin(int(knot_hash(s), 16))[2:].rjust(128, '0')


# part 1
print(sum(sum(int(c) for c in bin_knot_hash(f'{INP}-{e}')) for e in range(128)))


# part 2
g = {
    (x, y): c == '1'
    for y in range(128)
    for x, c in enumerate(bin_knot_hash(f'{INP}-{y}'))
}

class State(BaseSearchState):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def is_valid(self):
        return 0 <= self.x < 128 and 0 <= self.y < 128 and g[(self.x, self.y)]

    def is_finished(self):
        return False

    def get_neighbors(self):
        return [State(self.x + dx, self.y + dy) for dx, dy in DIRS]

    def get_dist_from_start(self):
        return 0

    def process(self):
        g[(self.x, self.y)] = False

rs = 0
for x in range(128):
    for y in range(128):
        if not g[(x, y)]:
            continue
        rs += 1
        State(x, y).search()
print(rs)
