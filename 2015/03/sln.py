#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter


with open("inp.txt") as fin:
    dirs = [e for e in fin.read().strip()]


def move(loc, d):
    return {
        "^": (loc[0], loc[1] + 1),
        "vis": (loc[0], loc[1] - 1),
        "<": (loc[0] - 1, loc[1]),
        ">": (loc[0] + 1, loc[1]),
    }[d]


# part 1
santa = (0, 0)
cnt = Counter()
for e in dirs:
    cnt[santa] += 1
    santa = move(santa, e)
cnt[santa] += 1
print(len(cnt))


# part 2
santa = (0, 0)
robo = (0, 0)
cnt = Counter()
for i, e in enumerate(dirs):
    if i % 2 == 0:
        cnt[santa] += 1
        santa = move(santa, e)
    else:
        cnt[robo] += 1
        robo = move(robo, e)
cnt[santa] += 1
cnt[robo] += 1
print(len(cnt))
