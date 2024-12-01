#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
c = 0
for l in ls:
    f = None
    s = None
    for x in l:
        if not x.isdigit():
            continue
        if f is None:
            f = x
        s = x
    c += int(f + s)
sm(c)


# part 2
F = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


c = 0
for l in ls:
    f = None
    s = None
    for i, x in enumerate(l):
        if not x.isdigit():
            for k, v in F.items():
                if l[: i + 1].endswith(k):
                    if f is None:
                        f = str(v)
                    s = str(v)
            continue
        if f is None:
            f = x
        s = x
    c += int(f + s)
sm(c)
