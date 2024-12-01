#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from web import *


# part 1
def run():
    spl = dt.split("\n\n")
    ns = [int(e) for e in spl[0].split(",")]
    bs = [
        {
            (x, y): [int(e), False]
            for y, l in enumerate(b.split("\n"))
            for x, e in enumerate(f for f in l.split(" ") if f)
        }
        for b in spl[1:]
    ]
    for n in ns:
        for b in bs:
            for v in b.values():
                if v[0] == n:
                    v[1] = True
            if any(
                all(b[(i, j)][1] for j in range(5))
                or all(b[(j, i)][1] for j in range(5))
                for i in range(5)
            ):
                sm(sum(e for e, f in b.values() if not f) * n)
                return


run()


# part 2
def run():
    spl = dt.split("\n\n")
    ns = [int(e) for e in spl[0].split(",")]
    bs = [
        {
            (x, y): [int(e), False]
            for y, l in enumerate(b.split("\n"))
            for x, e in enumerate(f for f in l.split(" ") if f)
        }
        for b in spl[1:]
    ]
    ws = [False for _ in range(len(bs))]
    for n in ns:
        for ind, b in enumerate(bs):
            if ws[ind]:
                continue
            for v in b.values():
                if v[0] == n:
                    v[1] = True
            if any(
                all(b[(i, j)][1] for j in range(5))
                or all(b[(j, i)][1] for j in range(5))
                for i in range(5)
            ):
                ws[ind] = True
                if all(ws):
                    sm(sum(e for e, f in b.values() if not f) * n)
                    return


run()
