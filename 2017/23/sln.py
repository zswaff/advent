#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict

from assembly import BaseAssembler


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
class Assembler(BaseAssembler):
    def __init__(self, lines):
        super().__init__(lines, defaultdict(int))
        self.c = 0

    def is_finished(self):
        return not 0 <= self.instr_idx < len(self.instrs)

    def get_result(self):
        return self.c

    def i__set(self, a, b):
        self.registers[a] = self.eval(b)

    def i__sub(self, a, b):
        self.registers[a] -= self.eval(b)

    def i__mul(self, a, b):
        self.registers[a] *= self.eval(b)
        self.c += 1

    def i__jnz(self, a, b):
        if self.eval(a) != 0:
            self.jump = self.eval(b)


print(Assembler(lines).run().result)


# part 2
f = lambda x: int(lines[x].split(" ")[-1])
h = 0
start = f(0) * f(4) - f(5)
stop = start - f(7) + 1
step = -f(-2)
for b in range(start, stop, step):
    for d in range(2, int(b**0.5) + 1):
        if b % d == 0:
            h += 1
            break
print(h)
