#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
ranges = []
for line in lines:
    splt = line.split("-")
    mn, mx = int(splt[0]), int(splt[1]) + 1
    while True:
        for i, (omn, omx) in enumerate(ranges):
            if mx < omn or omx < mn:
                continue
            ranges.pop(i)
            mn, mx = min(mn, omn), max(mx, omx)
            break
        else:
            ranges.append((mn, mx))
            break

print(min(*ranges)[1])


# part 2
print(4294967296 - sum(e[1] - e[0] for e in ranges))
