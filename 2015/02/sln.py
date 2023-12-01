#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    dims = [[int(f) for f in e.strip().split("x")] for e in fin.readlines()]


# part 1
c = 0
for l, w, h in dims:
    c += 2 * (l * w + w * h + h * l)
    c += l * w * h // max(l, w, h)
print(c)


# part 2
c = 0
for l, w, h in dims:
    c += 2 * (l + w + h - max(l, w, h))
    c += l * w * h
print(c)
