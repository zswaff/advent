#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations


with open("inp.txt") as fin:
    ls = [int(e.strip()) for e in fin.readlines()]


# part 1
for e, f in combinations(ls, 2):
    if e + f == 2020:
        print(e * f)
        break


# part 2
for e, f, g in combinations(ls, 3):
    if e + f + g == 2020:
        print(e * f * g)
        break
