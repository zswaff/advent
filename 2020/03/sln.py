#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
c = 0
for i, l in enumerate(lines):
    mi = (i * 3) % len(l)
    if l[mi] == "#":
        c += 1
print(c)


# part 2
p = 1
for s in [1, 3, 5, 7]:
    c = 0
    for i, l in enumerate(lines):
        mi = (i * s) % len(l)
        if l[mi] == "#":
            c += 1
    p *= c
c = 0
for i, l in enumerate(lines):
    if i % 2 == 1:
        continue
    mi = (i // 2) % len(l)
    if l[mi] == "#":
        c += 1
p *= c
print(p)
