#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
rv = defaultdict(set)
for l in ls:
    a, b = l.split(": ")
    spl = b.split(" ")
    for e in spl:
        rv[e].add(a)


@cache
def c(g, n):
    if n == g:
        return 1
    return sum(c(g, e) for e in rv[n])


sm(c("you", "out"))


# part 2
sm(
    c("svr", "dac") * c("dac", "fft") * c("fft", "out")
    + c("svr", "fft") * c("fft", "dac") * c("dac", "out")
)
