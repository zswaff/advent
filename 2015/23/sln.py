#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# todo convert to use assembly class


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


def exec_inp(regs):
    idx = 0
    while True:
        if idx >= len(lines):
            break
        cmd = lines[idx]
        ins, rest = cmd[:3], cmd[4:]
        if ins == "hlf":
            regs[rest] /= 2
            idx += 1
        if ins == "tpl":
            regs[rest] *= 3
            idx += 1
        if ins == "inc":
            regs[rest] += 1
            idx += 1
        if ins == "jmp":
            idx += int(rest)
        if ins == "jie":
            reg, off = rest.split(", ")
            if regs[reg] % 2 == 0:
                idx += int(off)
            else:
                idx += 1
        if ins == "jio":
            reg, off = rest.split(", ")
            if regs[reg] == 1:
                idx += int(off)
            else:
                idx += 1
    return regs


# part 1
print(exec_inp({"a": 0, "b": 0})["b"])


# part 2
print(exec_inp({"a": 1, "b": 0})["b"])
