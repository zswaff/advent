#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    lines = [int(e.strip()) for e in fin.readlines()]


# part 1
for i, e in enumerate(lines[25:]):
    s = set(lines[i : i + 25])
    if not any((n := e - f) != f and n in s for f in s):
        break
print(e)


# part 2
s = f = c = 0
while c != e:
    while c < e:
        c += lines[f]
        f += 1
    while c > e:
        c -= lines[s]
        s += 1
print(min(lines[s:f]) + max(lines[s:f]))
