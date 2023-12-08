#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
m = {e[:3]: e[7:-1].split(", ") for e in ls[2:]}
xs = [0 if e == "L" else 1 for e in ls[0]]
c = "AAA"
for i in count():
    c = m[c][xs[i % len(xs)]]
    if c == "ZZZ":
        sm(i + 1)
        break


# part 2
def reps(c):
    res = []
    vis = set()
    for i in count():
        idx = i % len(xs)
        c = m[c][xs[idx]]
        if c.endswith("Z"):
            res.append((i + 1, c))
            key = c, idx
            if key in vis:
                break
            vis.add(key)
    assert len(res) == 2 and res[0][1] == res[1][1]
    return res[0][0], res[1][0] - res[0][0]


(b, a), *rest = [reps(e) for e in m.keys() if e.endswith("A")]
for ob, oa in rest:
    nb = b
    for i in count():
        cand = nb - ob
        if cand > 0 and cand % oa == 0:
            break
        nb += a
    b = nb
    a = lcm(a, oa)
sm(b)
