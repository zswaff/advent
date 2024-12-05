#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
rso, ps = ss
rs = defaultdict(set)
for k, v in pas("{i}|{i}", rso):
    rs[k].add(v)
c = 0
for l in ps:
    d = set()
    spl = [int(e) for e in l.split(",")]
    for x in spl:
        if rs[x] & d:
            break
        d.add(x)
    else:
        c += spl[len(spl) // 2]
sm(c)


# part 2
rrs = defaultdict(set)
for v, k in pas("{i}|{i}", rso):
    rrs[k].add(v)
c = 0
for l in ps:
    d = set()
    spl = [int(e) for e in l.split(",")]
    for x in spl:
        if rs[x] & d:
            break
        d.add(x)
    else:
        continue

    res = []
    q = set(spl)
    while q:
        for e in q:
            if not rrs[e] & q:
                break
        q.remove(e)
        res.append(e)
    c += res[len(res) // 2]
sm(c)
