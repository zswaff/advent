#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
vs, rs = ss
vs = {e: f == "1" for e, f in pas("{}: {}", vs)}
bw = {f: e for *e, f in pas("{} {} {} -> {}", rs)}


@cache
def get(v):
    if v in vs:
        return vs[v]
    v1, op, v2 = bw[v]
    if op == "AND":
        return get(v1) and get(v2)
    if op == "OR":
        return get(v1) or get(v2)
    return get(v1) != get(v2)


s = "".join(
    str(int(get(e))) for e in sorted((e for e in bw if e[0] == "z"), reverse=True)
)
sm(int(s, 2))


# part 2
def test(vs, bw):
    worked = True
    for i in range(3):

        @cache
        def get(v):
            if v in vs:
                return vs[v]
            v1, op, v2 = bw[v]
            if op == "AND":
                return get(v1) and get(v2)
            if op == "OR":
                return get(v1) or get(v2)
            return get(v1) != get(v2)

    return worked
