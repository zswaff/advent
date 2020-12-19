#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    instrs = [e.strip() for e in fin.readlines()]


def run(regs):
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
        spl = instr.split(' ')
        cmd = spl[0]
        if cmd == 'cpy':
            regs[spl[2]] = eval_arg(spl[1])
            instr_ptr += 1
            continue
        if cmd == 'inc':
            regs[spl[1]] += 1
            instr_ptr += 1
            continue
        if cmd == 'dec':
            regs[spl[1]] -= 1
            instr_ptr += 1
            continue
        if cmd == 'jnz':
            if eval_arg(spl[1]) != 0:
                instr_ptr += eval_arg(spl[2])
            else:
                instr_ptr += 1
            continue
        if cmd == 'tgl':
            subj = eval_arg(spl[2])
    return regs


# part 1
print(run({'a': 7, 'b': 0, 'c': 0, 'd': 0})['a'])


# part 2
