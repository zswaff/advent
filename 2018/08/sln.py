#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from web import *


ns = [int(e) for e in dt.split()]


# part 1
def rec(inp):
    cs = inp[0]
    ms = inp[1]
    l = 2
    tcm = 0
    for i in range(cs):
        cl, cm = rec(inp[l:])
        l += cl
        tcm += cm
    return l + ms, tcm + sum(inp[l:l+ms])

sa(rec(ns)[1])


# part 2
def rec(inp):
    cs = inp[0]
    ms = inp[1]
    l = 2
    cvs = []
    for i in range(cs):
        cl, cv = rec(inp[l:])
        l += cl
        cvs.append(cv)
    v = sum(inp[l:l+ms])
    if cs != 0:
        v = sum(cvs[e-1] for e in inp[l:l+ms] if 1 <= e <= cs)
    return l + ms, v

sb(rec(ns)[1])
