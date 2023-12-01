#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


with open("inp.txt") as fin:
    exprs = [e.strip() for e in fin.readlines()]


# part 1
def evl(expr):
    while "(" in expr:
        s = expr.index("(")
        lvl = 1
        for i in range(s + 1, len(expr)):
            c = expr[i]
            if c == "(":
                lvl += 1
            if c == ")":
                lvl -= 1
            if lvl == 0:
                break
        expr = expr[:s] + str(evl(expr[s + 1 : i])) + expr[i + 1 :]
    splt = expr.split(" ")
    r = int(splt[0])
    for i in range(1, len(splt), 2):
        op, nxt = splt[i], int(splt[i + 1])
        if op == "+":
            r += nxt
        else:
            r *= nxt
    return r


print(sum(evl(e) for e in exprs))


# part 2
def evl(expr):
    while "(" in expr:
        s = expr.index("(")
        lvl = 1
        for i in range(s + 1, len(expr)):
            c = expr[i]
            if c == "(":
                lvl += 1
            if c == ")":
                lvl -= 1
            if lvl == 0:
                break
        expr = expr[:s] + str(evl(expr[s + 1 : i])) + expr[i + 1 :]
    splt = expr.split(" ")
    nums = [int(e) for e in splt[::-2]]
    ops = splt[-2::-2]
    for i, op in enumerate(ops):
        if op == "+":
            nums[i + 1] += nums[i]
            nums[i] = 1
    return math.prod(nums)


print(sum(evl(e) for e in exprs))
