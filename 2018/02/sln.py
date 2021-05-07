#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
print(sum(1 for e in lines if 2 in set(Counter(e).values())) *
      sum(1 for e in lines if 3 in set(Counter(e).values())))


# part 2
def fn():
    for i, e in enumerate(lines):
        for f in lines[i + 1:]:
            for j in range(len(e)):
                if e[:j] + e[j+1:] == f[:j] + f[j+1:]:
                    return e[:j] + e[j+1:]
print(fn())
