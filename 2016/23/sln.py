#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# todo convert to use assembly class


with open("inp.txt") as fin:
    orig_instrs = [e.strip().split(" ") for e in fin.readlines()]


def run(regs):
    instrs = [list(e) for e in orig_instrs]

    instr_ptr = 0

    def eval_arg(arg):
        try:
            return int(arg)
        except ValueError:
            return regs[arg]

    while True:
        if instr_ptr >= len(instrs):
            break
        instr = instrs[instr_ptr]
        cmd = instr[0]
        if cmd == "cpy":
            dest = instr[2]
            if dest in regs:
                regs[dest] = eval_arg(instr[1])
            instr_ptr += 1
            continue
        if cmd == "inc":
            regs[instr[1]] += 1
            instr_ptr += 1
            continue
        if cmd == "dec":
            regs[instr[1]] -= 1
            instr_ptr += 1
            continue
        if cmd == "jnz":
            if eval_arg(instr[1]) != 0:
                instr_ptr += eval_arg(instr[2])
            else:
                instr_ptr += 1
            continue
        if cmd == "tgl":
            subj_ptr = instr_ptr + regs[instr[1]]
            if subj_ptr < 0 or subj_ptr >= len(instrs):
                instr_ptr += 1
                continue
            oinstr = instrs[subj_ptr]
            if len(oinstr) == 2:
                if oinstr[0] == "inc":
                    oinstr[0] = "dec"
                else:
                    oinstr[0] = "inc"
            else:
                if oinstr[0] == "jnz":
                    oinstr[0] = "cpy"
                else:
                    oinstr[0] = "jnz"
            instr_ptr += 1
            continue
    return regs


# part 1
print(run({"a": 7, "b": 0, "c": 0, "d": 0})["a"])


# part 2
print(run({"a": 12, "b": 0, "c": 0, "d": 0})["a"])
