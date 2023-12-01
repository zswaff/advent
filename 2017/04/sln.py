#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
print(sum(Counter(l.split(" ")).most_common()[0][1] == 1 for l in lines))


# part 2
print(
    sum(Counter("".join(sorted(e)) for e in l.split(" ")).most_common()[0][1] == 1 for l in lines)
)
