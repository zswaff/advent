#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from assembly import *
from aoc import *
from web import *


class Assembler(BaseAssembler):
    def __init__(self, lines, regs, stop=None):
        super().__init__(lines[1:], defaultdict(int, regs))
        self.instr_idx_remap = int(lines[0].split(" ")[-1])
        self.stop = stop

    def is_finished(self):
        return not 0 <= self.instr_idx < len(self.instrs) or (
            self.stop is not None and self.step >= self.stop
        )

    def get_result(self):
        return [e[1] for e in sorted(self.registers.items())]

    def i__ip(self, a):
        self.instr_idx_remap = a
        self.instr_idx = self.registers[self.instr_idx_remap]

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

    def update_instr_idx(self):
        self.registers[self.instr_idx_remap] += 1
        self.instr_idx = self.registers[self.instr_idx_remap]


# part 1
sm(Assembler(ls, {}).run().result[0])


# part 2
fac = Assembler(ls, {0: 1}, 500).run().result[5]
sm(sum(i for i in range(1, fac + 1) if fac % i == 0))
