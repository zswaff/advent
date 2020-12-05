#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
def seat_id(s):
    def rec(rem, mn, mx):
        if rem == '':
            return mn
        ch = rem[0]
        hf = (mx - mn + 1) // 2
        if ch == 'R' or ch == 'B':
            return rec(rem[1:], mn + hf, mx)
        else:
            return rec(rem[1:], mn, mx - hf)
    return rec(s[:7], 0, 127) * 8 + rec(s[-3:], 0, 7)

ids = sorted(seat_id(e) for e in lines)
print(max(ids))


# part 2
for i in range(1, len(ids)):
    if ids[i - 1] + 2 == ids[i]:
        print(ids[i] - 1)
