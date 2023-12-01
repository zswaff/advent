#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]
scns = {}
for l in lines:
    k, v = [int(e) for e in l.split(": ")]
    scns[k] = v, v * 2 - 2


# part 1
print(sum(k * v for k, (v, r) in scns.items() if k % r == 0))


# part 2
for i in count():
    if all((i + k) % r != 0 for k, (_, r) in scns.items()):
        print(i)
        break
