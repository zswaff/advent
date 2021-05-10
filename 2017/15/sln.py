#!/usr/bin/env python3
# -*- coding: utf-8 -*-


MA, MB = 16807, 48271
MOD = 2147483647


with open('inp.txt') as fin:
    sa, sb = [int(e.strip().split()[-1]) for e in fin.readlines()]


# part 1
c = 0
ca, cb = sa, sb
for i in range(int(4e7)):
    ca = (ca * MA) % MOD
    cb = (cb * MB) % MOD
    if f'{ca:0>16b}'[-16:] == f'{cb:0>16b}'[-16:]:
        c += 1
print(c)


# part 2
c = 0
ca, cb = sa, sb
for i in range(int(5e6)):
    while True:
        ca = (ca * MA) % MOD
        if ca % 4 == 0:
            break
    while True:
        cb = (cb * MB) % MOD
        if cb % 8 == 0:
            break
    if f'{ca:0>16b}'[-16:] == f'{cb:0>16b}'[-16:]:
        c += 1
print(c)
