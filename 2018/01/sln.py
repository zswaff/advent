#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from web import *


nums = [int(e) for e in ls]


# part 1
sa(sum(nums))


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
sb(fn())
