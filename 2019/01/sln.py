#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    weights = [int(e.strip()) for e in fin.readlines()]


# part 1
def calc_fuel(w):
    return w//3 - 2

print(sum(calc_fuel(e) for e in weights))


# part 2
def calc_full_fuel(w):
    s = -w
    f = w
    while f > 0:
        s += f
        f = calc_fuel(f)
    return s

print(sum(calc_full_fuel(e) for e in weights))
