#!/usr/bin/env python3
# -*- coding: utf-8 -*-21


with open('inp.txt') as fin:
    lines = [e.strip().rsplit(' ', 1) for e in fin.readlines()]


# part 1
t = 10007
l = list(range(t))
for op, e in lines:
    if op == 'deal into new':
        l = list(reversed(l))
        continue
    if op == 'cut':
        l = l[int(e):] + l[:int(e)]
        continue
    if op == 'deal with increment':
        ol = list(l)
        for i in range(t):
            l[(i * int(e)) % t] = ol[i]
        continue
print(l.index(2019))


# part 2
# r = s
# for op, e in reversed(lines):
#     if op == 'deal into new':
#         r = t - r - 1
#         continue
#     if op == 'cut':
#         r = (r + e) % t
#         continue
#     if op == 'deal with increment':
#
#         continue
# print(r)
