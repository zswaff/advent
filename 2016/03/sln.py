#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    groups = [[int(f) for f in e.strip().split()] for e in fin.readlines()]


# part 1
tris = [sorted(e) for e in groups]
print(len([1 for a, b, c in tris if a + b > c]))


# part 2
tris = []
for i in range(0, len(groups), 3):
    for j in range(3):
        tris.append(sorted([groups[i][j], groups[i + 1][j], groups[i + 2][j]]))

print(len([1 for a, b, c in tris if a + b > c]))
