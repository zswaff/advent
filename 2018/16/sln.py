#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from assembly import *
from common import *
from web import *


class Assembler(BaseAssembler):
    def __init__(self, lines, mapping, regs):
        mlns = []
        for l in lines:
            spl = l.split(' ')
            mlns.append(' '.join([mapping[spl[0]]] + spl[1:]))
        super().__init__(mlns, dict(enumerate(regs)))

    def is_finished(self):
        return not 0 <= self.instr_idx < len(self.instrs)

    def get_result(self):
        return [e[1] for e in sorted(self.registers.items())]

    def i__addr(self, a, b, c):
        self.registers[c] = self.registers[a] + self.registers[b]

    def i__addi(self, a, b, c):
        self.registers[c] = self.registers[a] + b

    def i__mulr(self, a, b, c):
        self.registers[c] = self.registers[a] * self.registers[b]

    def i__muli(self, a, b, c):
        self.registers[c] = self.registers[a] * b

    def i__banr(self, a, b, c):
        self.registers[c] = self.registers[a] & self.registers[b]

    def i__bani(self, a, b, c):
        self.registers[c] = self.registers[a] & b

    def i__borr(self, a, b, c):
        self.registers[c] = self.registers[a] | self.registers[b]

    def i__bori(self, a, b, c):
        self.registers[c] = self.registers[a] | b

    def i__setr(self, a, b, c):
        self.registers[c] = self.registers[a]

    def i__seti(self, a, b, c):
        self.registers[c] = a

    def i__gtir(self, a, b, c):
        self.registers[c] = int(a > self.registers[b])

    def i__gtri(self, a, b, c):
        self.registers[c] = int(self.registers[a] > b)

    def i__gtrr(self, a, b, c):
        self.registers[c] = int(self.registers[a] > self.registers[b])

    def i__eqir(self, a, b, c):
        self.registers[c] = int(a == self.registers[b])

    def i__eqri(self, a, b, c):
        self.registers[c] = int(self.registers[a] == b)

    def i__eqrr(self, a, b, c):
        self.registers[c] = int(self.registers[a] == self.registers[b])


exs, lines = dt.split('\n\n\n\n')


# part 1
exs = exs.split('\n\n')
c = 0
mp = defaultdict(list)
for ex in exs:
    bef, instr, aft = ex.split('\n')
    bef = [int(e) for e in bef[9:-1].split(', ')]
    aft = [int(e) for e in aft[9:-1].split(', ')]
    innum = instr.split(' ')[0]
    pmp = {
        pin for pin in Assembler.get_possible_instrs()
        if Assembler([instr], {innum: pin}, bef).run().result == aft
    }
    mp[innum].append(pmp)
    if len(pmp) >= 3:
        c += 1
sm(c)


# part 2
imp = {k: set.intersection(*v) for k, v in mp.items()}
while any(len(e) != 1 for e in imp.values()):
    for k1, v1 in imp.items():
        if len(v1) != 1:
            continue
        for k2, v2 in imp.items():
            if k2 == k1:
                continue
            v2 -= v1
sm(Assembler(
    lines.split('\n'),
    {k: list(v)[0] for k, v in imp.items()},
    [0, 0, 0, 0]
).run().result[0])
