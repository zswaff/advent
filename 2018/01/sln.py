#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    nums = [int(e.strip()) for e in fin.readlines()]


# part 1
print(sum(nums))


# part 2
def fn():
    c = 0
    s = {c}
    while True:
        for e in nums:
            c += e
            if c in s:
                return c
            s.add(c)
print(fn())
