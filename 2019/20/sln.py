#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    lines = [e.strip('\n') + ' ' for e in fin.readlines()]
g = {(x, y): e for y, row in enumerate(lines) for x, e in enumerate(row)}


aa = None
zz = None
w = {}
for l, s in g.items():
    if s != '.':
        continue
    ns = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        n = l[0] + d[0], l[1] + d[1]
        if g[n] == '.':
            ns.append((n, 0))
        if 'A' <= g[n] <= 'Z':
            nn = n[0] + d[0], n[1] + d[1]
            p1, p2 = g[n], g[nn]
            ii = (nn[0] + d[0], nn[1] + d[1]) in g
            if p1 + p2 == 'AA':
                aa = l
                continue
            if p1 + p2 == 'ZZ':
                zz = l
                continue
            for l2, s2 in g.items():
                if s2 != p1 or l2 == n:
                    continue
                for d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    n2 = l2[0] + d2[0], l2[1] + d2[1]
                    if n2 not in g or g[n2] != p2:
                        continue
                    n2n = l2[0] - d2[0], l2[1] - d2[1]
                    if n2n not in g or g[n2n] != '.':
                        n2n = n2[0] + d2[0], n2[1] + d2[1]
                    ns.append((n2n, 1 if ii else -1))
                    break
    w[l] = ns


# part 1
# def bfs():
#     s = set()
#     q = [(aa, 0)]
#     while len(q) != 0:
#         l, d = q.pop(0)
#         s.add(l)
#         if l == zz:
#             return d
#         for n, _ in w[l]:
#             if n in s:
#                 continue
#             q.append((n, d + 1))
# print(bfs())


# part 2
def bfs():
    s = set()
    q = [((aa, 0), 0)]
    c = 0
    while len(q) != 0:
        lr, d = q.pop(0)
        c += 1
        if c % 10000 == 0:
            print(c, d)
        s.add(lr)
        if lr == (zz, 0):
            return d
        l, r = lr
        for ndr in w[l]:
            if ndr in s:
                continue
            n, dr = ndr
            if r + dr < 0:
                continue
            q.append(((n, r + dr), d + 1))
print(bfs())
