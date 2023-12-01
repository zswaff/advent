#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


# part 1
sm(sum(sum(1 for e in l.split(" | ")[1].split(" ") if len(e) in {2, 3, 4, 7}) for l in ls))


# part 2
nl = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
nd = {e: i for i, e in enumerate(nl)}
c = 0
for l in ls:
    l1, l2 = [e.split(" ") for e in l.split(" | ")]
    for t in permutations("abcdefg"):
        u = dict(zip("abcdefg", t))
        if all("".join(sorted(u[f] for f in e)) in nd for e in l1):
            c += int("".join(str(nd["".join(sorted(u[f] for f in e))]) for e in l2))
            break
sm(c)
