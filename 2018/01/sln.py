#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


nums = [int(e) for e in lines]


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
