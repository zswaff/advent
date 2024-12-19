#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
os, ts = ss
os = os[0].split(", ")


@cache
def r(x):
    if len(x) == 0:
        return True
    return any(x.startswith(e) and r(x[len(e) :]) for e in os)


sm(sum(r(e) for e in ts))


# part 2
@cache
def r(x):
    if len(x) == 0:
        return 1
    return sum(r(x[len(e) :]) for e in os if x.startswith(e))


sm(sum(r(e) for e in ts))
