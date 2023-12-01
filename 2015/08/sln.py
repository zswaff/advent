#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
print(sum(len(e) - len(eval(e)) for e in lines))

# part 2
tot = 0
for line in lines:
    tot += 2
    tot += line.count("\\")
    tot += line.count('"')
print(tot)
