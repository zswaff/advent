#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


root = {}
root[".."] = root
curr = root
for s in dt[2:].split("\n$ "):
    ls = s.split("\n")
    cmd = ls[0]
    if cmd.startswith("cd"):
        dest = cmd[3:]
        if dest == "/":
            curr = root
            continue
        curr = curr[dest]
        continue
    for l in ls[1:]:
        t, n = l.split(" ")
        if t == "dir":
            curr[n] = {}
            curr[n][".."] = curr
            continue
        curr[n] = int(t)


# part 1
smalls = []


def rec(n):
    if isinstance(n, int):
        return n
    sz = sum(rec(v) for k, v in n.items() if k != "..")
    if sz < 100000:
        smalls.append(sz)
    return sz


rec(root)
sm(sum(smalls))


# part 2
szs = []


def rec(n):
    if isinstance(n, int):
        return n
    sz = sum(rec(v) for k, v in n.items() if k != "..")
    szs.append(sz)
    return sz


tot = rec(root)
szs.sort()
mn = 30000000 - (70000000 - tot)
sm(next(e for e in szs if e >= mn))
