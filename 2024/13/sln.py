#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
c = 0
for s in ss:
    ax, ay = pa("Button A: X{i}, Y{i}", s[0])
    bx, by = pa("Button B: X{i}, Y{i}", s[1])
    px, py = pa("Prize: X={i}, Y={i}", s[2])

    class State(BaseSearchState):
        def __init__(self, ac, bc, dist):
            super().__init__()
            self.ac = ac
            self.bc = bc
            self.dist = dist

        def is_valid(self):
            return self.ac <= 100 and self.bc <= 100

        def is_finished(self):
            return (
                self.ac * ax + self.bc * bx == px and self.ac * ay + self.bc * by == py
            )

        def get_neighbors(self):
            return [
                State(self.ac + 1, self.bc, self.dist + 3),
                State(self.ac, self.bc + 1, self.dist + 1),
            ]

    dc = State(0, 0, 0).search().distance
    if dc is None:
        continue
    c += dc
sm(c)


# part 2
c = 0
for s in ss:
    ax, ay = pa("Button A: X{i}, Y{i}", s[0])
    bx, by = pa("Button B: X{i}, Y{i}", s[1])
    px, py = pa("Prize: X={i}, Y={i}", s[2])
    px += 10000000000000
    py += 10000000000000

    opt = z3.Optimize()
    A = z3.Int("A")
    B = z3.Int("B")
    opt.add(ax * A + bx * B == px)
    opt.add(ay * A + by * B == py)
    objective = 3 * A + B

    opt.minimize(objective)
    if opt.check() != z3.sat:
        continue
    model = opt.model()
    c += 3 * model[A].as_long() + model[B].as_long()
sm(c)
