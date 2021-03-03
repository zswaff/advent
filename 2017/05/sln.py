#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


with open('inp.txt') as fin:
    lines = [int(e.strip()) for e in fin.readlines()]


# part 1
idx = 0
for i in count():
    c = lines[idx]
    lines[idx] += 1
    idx += c
    if not 0 <= idx < len(lines):
        break
print(i + 1)


# part 2
idx = 0
for i in count():
    c = lines[idx]
    lines[idx] += -1 if c >= 3 else 1
    idx += c
    if not 0 <= idx < len(lines):
        break
print(i + 1)
