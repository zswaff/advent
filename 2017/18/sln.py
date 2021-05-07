#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict

from assembly import BaseAssembler


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
class Assembler(BaseAssembler):
    def __init__(self, lines):
        super().__init__(lines, defaultdict(int))
        self.finished = False
        self.out = []

    def is_finished(self):
        return self.finished or not 0 <= self.instr_idx < len(self.instrs)

    def get_result(self):
        return self.out[-1]

    def i__snd(self, a):
        self.out.append(self.eval(a))

    def i__set(self, a, b):
        self.registers[a] = self.eval(b)

    def i__add(self, a, b):
        self.registers[a] += self.eval(b)

    def i__mul(self, a, b):
        self.registers[a] *= self.eval(b)

    def i__mod(self, a, b):
        self.registers[a] %= self.eval(b)

    def i__rcv(self, a):
        if self.eval(a) != 0:
            self.finished = True

    def i__jgz(self, a, b):
        if self.eval(a) > 0:
            self.jump = self.eval(b)

print(Assembler(lines).run().result)


# part 2
class Assembler(BaseAssembler):
    def __init__(self, lines, registers, other=None):
        super().__init__(lines, registers)
        self.other = other
        self.inp = []
        self.inp_idx = 0
        self.out = []
        self.finished = False
        self.paused = False

    def is_finished(self):
        return self.finished or not 0 <= self.instr_idx < len(self.instrs)

    def is_paused(self):
        return self.paused

    def get_result(self):
        return len(self.out)

    def i__set(self, a, b):
        self.registers[a] = self.eval(b)

    def i__add(self, a, b):
        self.registers[a] += self.eval(b)

    def i__mul(self, a, b):
        self.registers[a] *= self.eval(b)

    def i__mod(self, a, b):
        self.registers[a] %= self.eval(b)

    def i__jgz(self, a, b):
        if self.eval(a) > 0:
            self.jump = self.eval(b)

    def i__snd(self, a):
        v = self.eval(a)
        self.out.append(v)
        if self.other is not None:
            self.other.inp.append(v)

    def i__rcv(self, a):
        if self.inp_idx >= len(self.inp):
            if self.other is None:
                self.paused = True
                self.jump = 0
                return

            self.other.paused = False
            self.other.run()
            self.inp = self.other.out

        if self.inp_idx >= len(self.inp):
            self.finished = True
            return

        self.registers[a] = self.inp[self.inp_idx]
        self.inp_idx += 1


p0 = Assembler(lines, {'p': 0, 'x': 1})
print(Assembler(lines, {'p': 1, 'x': 0}, p0).run().result)