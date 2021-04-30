#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# assembly


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
def run(instrs):
    acc = 0
    idx = 0
    visited = set()
    finished = False
    while True:
        if idx in visited:
            break
        if idx == len(instrs):
            finished = True
            break
        visited.add(idx)
        cmd, amt = instrs[idx].split(' ')
        if cmd == 'nop':
            idx += 1
            continue
        if cmd == 'acc':
            acc += int(amt)
            idx += 1
            continue
        idx += int(amt)
    return acc, finished
print(run(lines)[0])


# part 2
for i, l in enumerate(lines):
    if l.startswith('acc'):
        continue
    if l.startswith('nop'):
        nl = 'jmp' + l[3:]
    else:
        nl = 'nop' + l[3:]
    a, f = run(lines[:i] + [nl] + lines[i+1:])
    if f:
        print(a)