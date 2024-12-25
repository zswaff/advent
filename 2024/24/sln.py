#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
vs, rs = ss
vs = {e: f == "1" for e, f in pas("{}: {}", vs)}
bw = {f: e for *e, f in pas("{} {} {} -> {}", rs)}

l = []


@cache
def get(v):
    if v in vs:
        r = vs[v]
        l.append((v, r))
        return r
    v1, op, v2 = bw[v]
    if op == "AND":
        r = get(v1) and get(v2)
        l.append((v, r))
        return r
    if op == "OR":
        r = get(v1) or get(v2)
        l.append((v, r))
        return r
    r = get(v1) != get(v2)
    l.append((v, r))
    return r


s = "".join(
    str(int(get(e))) for e in sorted((e for e in bw if e[0] == "z"), reverse=True)
)
sm(int(s, 2))


# part 2
