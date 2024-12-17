#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
A, B, C = "A", "B", "C"
R = {4: A, 5: B, 6: C}


class Assembler(BaseAssembler):
    def __init__(self, lines, registers, print_idxs=None):
        super().__init__(lines, registers, print_idxs)
        self.instr_idx_delta = 2
        self.jump_abs = True

        self.out = []

    def process_lines(self, lines):
        return [int(e) for e in lines.split(",")]

    def is_finished(self):
        return self.instr_idx >= len(self.instrs) - 1

    def get_result(self):
        return ",".join(str(e) for e in self.out)

    def get_cmd_and_args(self):
        return self.instrs[self.instr_idx], [self.instrs[self.instr_idx + 1]]

    def combo(self, x):
        if x <= 3:
            return x
        return self.registers[R[x]]

    def i__0(self, x):
        self.registers[A] = self.registers[A] // (2 ** self.combo(x))

    def i__1(self, x):
        self.registers[B] = self.registers[B] ^ x

    def i__2(self, x):
        self.registers[B] = self.combo(x) % 8

    def i__3(self, x):
        if self.registers[A] == 0 or x == self.instr_idx:
            return
        self.jump = x

    def i__4(self, x):
        self.registers[B] = self.registers[B] ^ self.registers[C]

    def i__5(self, x):
        self.out.append(self.combo(x) % 8)

    def i__6(self, x):
        self.registers[B] = self.registers[A] // (2 ** self.combo(x))

    def i__7(self, x):
        self.registers[C] = self.registers[A] // (2 ** self.combo(x))


rrs, p = ss
p = pa("Program: {}", p[0])[0]
ia = pa("Register A: {i}", rrs[0])[0]
ib = pa("Register B: {i}", rrs[1])[0]
ic = pa("Register C: {i}", rrs[2])[0]
sm(Assembler(p, {A: ia, B: ib, C: ic}).run().result)


# part 2
c = [""]
while True:
    worked = False
    nc = []
    for e in c:
        for i in range(8):
            ni = f"{e}{i}"
            r = Assembler(p, {A: int(ni, 8), B: ib, C: ic}).run().result
            if p.endswith(r):
                nc.append(ni)
            if r == p:
                worked = True
    c = nc
    if worked:
        break
sm(int(c[0], 8))
