#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from comp import Comp


# part 1
cmp = Comp(fin='inp.txt')
v = ''.join(chr(e) for e in cmp.outputs).strip()
m = [list(f) for f in v.split('\n')]
print(sum(
    x * y
    for y, row in enumerate(m[1:-1], 1)
    for x, e in enumerate(row[1:-1], 1)
    if e == m[y + 1][x] == m[y - 1][x] == m[y][x + 1] == m[y][x - 1]  == '#'
))


# part 2
print(v)

DIRS = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}
CHRS = {'^': 0, '>': 1, 'v': 2, '<': 3}

sloc, sdr = None, None
n = {}
for y, row in enumerate(m):
    for x, e in enumerate(row):
        n[(x, y)] = e != '.'
        if e in CHRS:
            sloc, sdr = (x, y), CHRS[e]

loc, dr = sloc, sdr
rt = []
while True:
    nloc = loc[0] + DIRS[dr][0], loc[1] + DIRS[dr][1]
    while n.get(nloc, False):
        rt[-1][1] += 1
        loc = nloc
        nloc = loc[0] + DIRS[dr][0], loc[1] + DIRS[dr][1]
    ndr = (dr - 1) % 4
    nloc = loc[0] + DIRS[ndr][0], loc[1] + DIRS[ndr][1]
    if n.get(nloc, False):
        rt.append(['L', 0])
        dr = ndr
        continue
    ndr = (dr + 1) % 4
    nloc = loc[0] + DIRS[ndr][0], loc[1] + DIRS[ndr][1]
    if n.get(nloc, False):
        rt.append(['R', 0])
        dr = ndr
        continue
    break

rt = [tuple(e) for e in rt]
rtm = {}
rts = []
for e in rt:
    if e not in rtm:
        rtm[e] = len(rtm)
    rts.append(rtm[e])

# todo generate these
A = [0, 1, 2]
B = [2, 0, 3, 2]
C = [0, 1, 1]
main = ['A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'A']
