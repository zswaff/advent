#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


with open("inp.txt") as fin:
    mvs = fin.read().strip().split(",")


def dance(ps):
    for mv in mvs:
        m, d = mv[0], mv[1:]
        if m == "s":
            d = int(d)
            ps = ps[-d:] + ps[:-d]
            continue
        if m == "x":
            a, b = [int(e) for e in d.split("/")]
            ps[a], ps[b] = ps[b], ps[a]
            continue
        a, b = [ps.index(e) for e in d.split("/")]
        ps[a], ps[b] = ps[b], ps[a]
    return ps


# part 1
print("".join(dance([chr(ord("a") + i) for i in range(16)])))


# part 2
ls = [[chr(ord("a") + i) for i in range(16)]]
for _ in count():
    t = dance([e for e in ls[-1]])
    if t == ls[0]:
        break
    ls.append(t)
print("".join(ls[int(1e9) % len(ls)]))
