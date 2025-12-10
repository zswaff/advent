#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
ps = []
for l in ls:
    a, *b, c = l.split()
    ps.append(
        (
            [e == "#" for e in a[1:-1]],
            [set(int(f) for f in e[1:-1].split(",")) for e in b],
            [int(e) for e in c[1:-1].split(",")],
        )
    )

c = 0
for ts, bs, _ in ps:
    opt = z3.Optimize()
    P = z3.IntVector("P", len(bs))
    for p in P:
        opt.add(p >= 0)
    for i, t in enumerate(ts):
        opt.add(z3.Sum([P[j] for j in range(len(bs)) if i in bs[j]]) % 2 == int(t))
    objective = z3.Sum(P)
    opt.minimize(objective)
    if opt.check() != z3.sat:
        raise RuntimeError("No solution found")
    model = opt.model()
    c += model.eval(objective).as_long()
sm(c)


# part 2
c = 0
for _, bs, ts in ps:
    opt = z3.Optimize()
    P = z3.IntVector("P", len(bs))
    for p in P:
        opt.add(p >= 0)
    for i, t in enumerate(ts):
        opt.add(z3.Sum([P[j] for j in range(len(bs)) if i in bs[j]]) == t)
    objective = z3.Sum(P)
    opt.minimize(objective)
    if opt.check() != z3.sat:
        raise RuntimeError("No solution found")
    model = opt.model()
    c += model.eval(objective).as_long()
sm(c)
