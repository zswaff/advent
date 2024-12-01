#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *
from web import *


ls1, ls2 = dt.split("\n\n")
dots = {(int(e), int(f)) for e, f in [g.split(",") for g in ls1.split("\n")]}
folds = [(e, int(f)) for e, f in [g[11:].split("=") for g in ls2.split("\n")]]


# part 1
d, l = folds[0]
if d == "x":
    dots = {(x if x < l else 2 * l - x, y) for x, y in dots}
if d == "y":
    dots = {(x, y if y < l else 2 * l - y) for x, y in dots}
sm(len(dots))


# part 2
for d, l in folds[1:]:
    if d == "x":
        dots = {(x if x < l else 2 * l - x, y) for x, y in dots}
    if d == "y":
        dots = {(x, y if y < l else 2 * l - y) for x, y in dots}
mxx, mxy = max(e[0] for e in dots), max(e[1] for e in dots)
for y in range(mxy + 1):
    for x in range(mxx + 1):
        print("#" if (x, y) in dots else " ", end="")
    print()
sm("RZKZLPGH")
