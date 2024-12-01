#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
rins, rps = ss
inm = {}
for e in rins:
    k, rv = e[:-1].split("{")
    inm[k] = rv.split(",")
ps = []
for e in rps:
    rvs = e[1:-1].split(",")
    p = {}
    for rv in rvs:
        k, v = rv.split("=")
        p[k] = int(v)
    ps.append(p)

c = 0
for p in ps:
    wf = "in"
    while True:
        ins = inm[wf]
        for instr in ins:
            spl = instr.split(":")
            if len(spl) == 1:
                wf = instr
                break
            cond, dest = spl
            if ">" in cond:
                a, b = cond.split(">")
                if p[a] > int(b):
                    wf = dest
                    break
            if "<" in cond:
                a, b = cond.split("<")
                if p[a] < int(b):
                    wf = dest
                    break
        if wf in {"A", "R"}:
            acc = wf == "A"
            break
    if acc:
        c += sum(p.values())
sm(c)


# part 2
def intersect(p1, p2):
    res = {
        k: (
            max(p1[k][0], p2.get(k, (1, 4001))[0]),
            min(p1[k][1], p2.get(k, (1, 4001))[1]),
        )
        for k in p1
    }
    if any(mx <= mn for mn, mx in res.values()):
        return None
    return res


res = []
q = [("R", {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)})]
while q:
    wf, p = q.pop()
    if p is None:
        continue
    if wf == "in":
        res.append(p)
        continue
    for nwf, ins in inm.items():
        np = p.copy()
        for instr in ins:
            if np is None:
                break
            spl = instr.split(":")
            if len(spl) == 1:
                if instr == wf:
                    q.append((nwf, np))
                continue
            cond, dest = spl
            if ">" in cond:
                a, b = cond.split(">")
                if dest == wf:
                    q.append((nwf, intersect(np, {a: (int(b) + 1, 4001)})))
                np = intersect(np, {a: (1, int(b) + 1)})
                continue
            if "<" in cond:
                a, b = cond.split("<")
                if dest == wf:
                    q.append((nwf, intersect(np, {a: (1, int(b))})))
                np = intersect(np, {a: (int(b), 4001)})
                continue

sm(4000**4 - sum(prod(mx - mn for mn, mx in e.values()) for e in res))
