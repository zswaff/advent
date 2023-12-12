#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
@cache
def recurve(s, gs):
    s = s.lstrip(".")
    if len(gs) == 0:
        return 1 if all(e != "#" for e in s) else 0
    if s == "":
        return 0
    if s.startswith("?"):
        return recurve(s[1:], gs) + recurve("#" + s[1:], gs)
    nreq = gs[0]
    if nreq > len(s):
        return 0
    if any(e == "." for e in s[:nreq]):
        return 0
    if not (nreq == len(s) or s[nreq] != "#"):
        return 0
    return recurve(s[nreq + 1 :], gs[1:])


c = 0
for l in ls:
    spl = l.split(" ")
    c += recurve(spl[0], tuple(int(e) for e in spl[1].split(",")))
sm(c)


# part 2
c = 0
for l in ls:
    spl = l.split(" ")
    c += recurve("?".join([spl[0]] * 5), tuple(int(e) for e in spl[1].split(",") * 5))
sm(c)
