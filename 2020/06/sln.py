#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    groups = [[set(f) for f in e.split("\n")] for e in fin.read().strip().split("\n\n")]


# part 1
print(sum(len(e[0].union(*e[1:])) for e in groups))


# part 2
print(sum(len(e[0].intersection(*e[1:])) for e in groups))
