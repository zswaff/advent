#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
instrs = re.findall(r"mul\(\d+,\d+\)", dt)
c = 0
for instr in instrs:
    a, b = pa(instr, "mul({i},{i})")
    c += a * b
sm(c)


# part 2
instrs = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", dt)
c = 0
on = True
for instr in instrs:
    i, r = pa(instr, ["mul({i},{i})", "do()", "don't()"])
    if i != 0:
        on = i == 1
        continue
    if on:
        c += r[0] * r[1]
sm(c)
