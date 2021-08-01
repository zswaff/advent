#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict


with open('inp.txt') as fin:
    groups = [e.strip().split('\n') for e in fin.read().split('\n\n')]


# part 1
state = groups[0][0][-2]
steps = int(groups[0][1].split(' ')[-2])
rules = {}
for lines in groups[1:]:
    name = lines[0][-2]
    for i in range(2):
        off = 2 + i * 4
        write = int(lines[off][-2])
        move = 1 if lines[off + 1][:-1].split(' ')[-1] == 'right' else -1
        nxt = lines[off + 2][-2]
        rules[(name, i)] = write, move, nxt

tape = defaultdict(int)
head = 0
for i in range(steps):
    val = tape[head]
    write, move, state = rules[(state, val)]
    tape[head] = write
    head += move
print(sum(tape.values()))
