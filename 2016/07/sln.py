#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
count = 0
for line in lines:
    valid = False
    invalid = False
    bracket_level = 0
    for i in range(len(line) - 3):
        c1, c2, c3, c4 = line[i:i + 4]
        if c1 == '[':
            bracket_level += 1
            continue
        if c1 == ']':
            bracket_level -= 1
            continue
        if c1 != c2 and c1 == c4 and c2 == c3:
            if bracket_level <= 0:
                valid = True
            else:
                invalid = True
    if valid and not invalid:
        count += 1
print(count)


# part 2
count = 0
for line in lines:
    outer_pairs = set()
    inner_pairs = set()
    bracket_level = 0
    for i in range(len(line) - 2):
        c1, c2, c3 = line[i:i + 3]
        if c1 == '[':
            bracket_level += 1
            continue
        if c1 == ']':
            bracket_level -= 1
            continue
        if c1 != c2 and c1 == c3:
            if bracket_level <= 0:
                outer_pairs.add((c1, c2))
            else:
                inner_pairs.add((c2, c1))
    if inner_pairs & outer_pairs:
        count += 1
print(count)
