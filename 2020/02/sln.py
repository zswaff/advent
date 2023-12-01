#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
c = 0
for l in lines:
    p1, pw = l.split(": ")
    p2, ltr = p1.split(" ")
    mn, mx = p2.split("-")
    if int(mn) <= Counter(pw).get(ltr, 0) <= int(mx):
        c += 1
print(c)


# part 2
c = 0
for l in lines:
    p1, pw = l.split(": ")
    p2, ltr = p1.split(" ")
    mn, mx = p2.split("-")
    d = dict(enumerate(pw))
    if (d[int(mn) - 1] == ltr) ^ (d[int(mx) - 1] == ltr):
        c += 1
print(c)
