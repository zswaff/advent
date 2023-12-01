#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    inp = fin.read().strip()


# part 1
total = 0
level = 0
skip = False
garbage = False
for c in inp:
    if skip:
        skip = False
        continue
    if c == "!":
        skip = True
        continue
    if garbage:
        if c == ">":
            garbage = False
        continue
    if c == "<":
        garbage = True
        continue
    if c == "}":
        total += level
        level -= 1
        continue
    if c == "{":
        level += 1
        continue
print(total)


# part 2
total = 0
skip = False
garbage = False
for c in inp:
    if skip:
        skip = False
        continue
    if c == "!":
        skip = True
        continue
    if garbage:
        if c == ">":
            garbage = False
        else:
            total += 1
        continue
    if c == "<":
        garbage = True
        continue
print(total)
