#!/usr/bin/env python3
# -*- coding: utf-8 -*-


INP = '10010000000110000'


def solve(n):
    t = INP
    while len(t) < n:
        m = reversed(t)
        t += '0'
        for c in m:
            t += '0' if c == '1' else '1'
    t = t[:n]
    while len(t) % 2 == 0:
        m = ''
        for i in range(0, len(t), 2):
            m += '1' if t[i] == t[i + 1] else '0'
        t = m
    return t


# part 1
print(solve(272))


# part 2
print(solve(35651584))
