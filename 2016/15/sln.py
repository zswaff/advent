#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


INP = [(15, 17), (2, 3), (4, 19), (2, 13), (2, 7), (0, 5)]


def solve():
    for i in count():
        for j, (st, tps) in enumerate(INP, 1):
            if (st + i + j) % tps != 0:
                break
        else:
            return i


# part 1
print(solve())


# part 2
INP.append((0, 11))
print(solve())
