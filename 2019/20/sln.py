#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import deque, defaultdict
from heapq import heappush, heappop


with open("inp.txt") as fin:
    lines = [e.strip("\n") + " " for e in fin.readlines()]
g = {(x, y): e for y, row in enumerate(lines) for x, e in enumerate(row)}


# part 1
aa = None
zz = None
w = {}
for l, s in g.items():
    if s != ".":
        continue
    ns = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        n = l[0] + d[0], l[1] + d[1]
        if g[n] == ".":
            ns.append((n, 0))
        if "A" <= g[n] <= "Z":
            nn = n[0] + d[0], n[1] + d[1]
            p1, p2 = g[n], g[nn]
            ii = (nn[0] + d[0], nn[1] + d[1]) in g
            if p1 + p2 == "AA":
                aa = l
                continue
            if p1 + p2 == "ZZ":
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
                    if n2n not in g or g[n2n] != ".":
                        n2n = n2[0] + d2[0], n2[1] + d2[1]
                    ns.append((n2n, 1 if ii else -1))
                    break
    w[l] = ns


def bfs():
    s = set()
    q = [(aa, 0)]
    while len(q) != 0:
        l, d = q.pop(0)
        s.add(l)
        if l == zz:
            return d
        for n, _ in w[l]:
            if n in s:
                continue
            q.append((n, d + 1))


print(bfs())


# part 2
w = defaultdict(dict)
ps = {}
pm = {}
for l, s in g.items():
    if not "A" <= s <= "Z":
        continue
    ns = {}
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        n = l[0] + d[0], l[1] + d[1]
        ns[g.get(n)] = n, d
    if "." not in ns:
        continue
    ll, lld = ns["."]
    ss = "".join(sorted([[k for k in ns.keys() if "A" <= k <= "Z"][0], s]))
    ps[ll] = ss
    if ss not in pm:
        pm[ss] = ll
        continue
    lml = l[0] - 2 * lld[0], l[1] - 2 * lld[1]
    dd = 1 if lml in g and lml[0] != max(e[0] for e in g.keys()) else -1
    w[ll][pm[ss]] = 1, dd
    w[pm[ss]][ll] = 1, -dd
aa, zz = pm["AA"], pm["ZZ"]


def fill_w(p):
    s = set()
    q = deque([(p, 0)])
    while len(q) != 0:
        l, c = q.popleft()
        s.add(l)
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n = l[0] + d[0], l[1] + d[1]
            if n in s or g.get(n) != ".":
                continue
            if n in ps:
                w[p][n] = c + 1, 0
            q.append((n, c + 1))


for p in ps:
    fill_w(p)


def bfs():
    s = set()
    q = [(0, (aa, 0))]
    while len(q) != 0:
        d, lr = heappop(q)
        s.add(lr)
        l, r = lr
        for n, (dd, dr) in w[l].items():
            nr = r + dr
            nlr = n, nr
            if nr < 0 or nlr in s:
                continue
            if nlr == (zz, 0):
                return d + dd
            heappush(q, (d + dd, nlr))


print(bfs())
