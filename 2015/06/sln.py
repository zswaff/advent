#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


CMD_FMT = r"(?P<cmd>turn on|toggle|turn off) (?P<tlx>\d{1,3}),(?P<tly>\d{1,3}) through (?P<brx>\d{1,3}),(?P<bry>\d{1,3})"


with open("inp.txt") as fin:
    instrs = [e.strip() for e in fin.readlines()]


# part 1
lights = [[False] * 1000 for _ in range(1000)]
for instr in instrs:
    params = re.match(CMD_FMT, instr).groupdict()
    cmd = params["cmd"]
    tlx, tly, brx, bry = [int(params[e]) for e in ["tlx", "tly", "brx", "bry"]]
    for x in range(tlx, brx + 1):
        for y in range(tly, bry + 1):
            lights[x][y] = {"turn on": True, "toggle": not lights[x][y], "turn off": False}[cmd]
print(sum(sum(e) for e in lights))


# part 2
lights = [[0] * 1000 for _ in range(1000)]
for instr in instrs:
    params = re.match(CMD_FMT, instr).groupdict()
    cmd = params["cmd"]
    tlx, tly, brx, bry = [int(params[e]) for e in ["tlx", "tly", "brx", "bry"]]
    for x in range(tlx, brx + 1):
        for y in range(tly, bry + 1):
            lights[x][y] += {"turn on": 1, "toggle": 2, "turn off": -1}[cmd]
            lights[x][y] = max(lights[x][y], 0)
print(sum(sum(e) for e in lights))
