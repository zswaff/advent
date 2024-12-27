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


b = "".join(
    str(int(get(e))) for e in sorted((e for e in bw if e[0] == "z"), reverse=True)
)
sm(int(b, 2))


# part 2
b = set()
m = set()
for t, (s1, op, s2) in bw.items():
    if t[0] != "z":
        continue
    n = t[1:]
    if op != "XOR":
        b.add(t)
        continue
    if t == "z00":
        continue
    nm = f"{int(n) - 1:02}"
    s1op = bw[s1][1]
    if s1op == "AND":
        b.add(s1)
        continue
    s2op = bw[s2][1]
    if s2op == "AND":
        b.add(s2)
        continue
    if {s1op, s2op} != {"OR", "XOR"}:
        b |= {s1, s2}
        m |= {s1, s2}
        continue
    ort, xort = (s1, s2) if s1op == "OR" else (s2, s1)
    xors1, _, xors2 = bw[xort]
    if {xors1, xors2} != {f"x{n}", f"y{n}"}:
        b.add(xort)
        continue
    ors1, _, ors2 = bw[ort]
    s1s1, s1op, s1s2 = bw[ors1]
    if s1op != "AND":
        b.add(ors1)
        continue
    s2s1, s2op, s2s2 = bw[ors2]
    if s2op != "AND":
        b.add(ors2)
        continue
    andt = ors1
    if {s2s1, s2s2} != {f"x{nm}", f"y{nm}"}:
        andt = ors2
        if {s1s1, s1s2} != {f"x{nm}", f"y{nm}"}:
            b |= {ors1, ors2}
            m |= {ors1, ors2}
            continue
    ands1, _, ands2 = bw[andt]
    # more to check here from this point


# import graphviz as gv

# dot = gv.Digraph(comment="chart")
# for t, (s1, op, s2) in bw.items():
#     if t in m:
#         dot.node(t, style="filled", color="yellow")
#     elif t in b:
#         dot.node(t, style="filled", color="red")
#     else:
#         dot.node(t)
# for t, (s1, op, s2) in bw.items():
#     x = f"{s1} {op} {s2} -> {t}"
#     dot.node(x, op)
#     dot.edge(s1, x)
#     dot.edge(s2, x)
#     dot.edge(x, t)
# dot.render(f"2024/24/chart", format="png", cleanup=True)

sm(",".join(sorted(b - {"gmk", "dsj", "z45"})))
