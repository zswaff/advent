#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import re
from itertools import count


FMT = r"<x=(?P<x>-?\d+), y=(?P<y>-?\d+), z=(?P<z>-?\d+)>"


def sign(a):
    if a == 0:
        return 0
    return 1 if a > 0 else -1


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


class Moon:
    def __init__(self, s):
        match = re.match(FMT, s).groupdict()
        self.x, self.y, self.z = [int(match[e]) for e in ["x", "y", "z"]]
        self.nx, self.ny, self.nz = 0, 0, 0
        self.dx, self.dy, self.dz = 0, 0, 0

    def uvel(self, others):
        for e in others:
            self.dx += sign(e.x - self.x)
            self.dy += sign(e.y - self.y)
            self.dz += sign(e.z - self.z)
        return self

    def upos(self):
        self.nx = self.x + self.dx
        self.ny = self.y + self.dy
        self.nz = self.z + self.dz
        return self

    def finalize(self):
        self.x = self.nx
        self.y = self.ny
        self.z = self.nz
        return self

    @property
    def pe(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def ke(self):
        return abs(self.dx) + abs(self.dy) + abs(self.dz)


# part 1
with open("inp.txt") as fin:
    moons = [Moon(e.strip()) for e in fin.readlines()]

for _ in range(1000):
    [e.uvel(moons).upos() for e in moons]
    [e.finalize() for e in moons]
print(sum(e.pe * e.ke for e in moons))


# part 2
with open("inp.txt") as fin:
    moons = [Moon(e.strip()) for e in fin.readlines()]

xs, ys, zs = set(), set(), set()
xrep, yrep, zrep = None, None, None
for _ in count():
    if not xrep:
        cx = tuple((e.x, e.dx) for e in moons)
        if cx in xs:
            xrep = len(xs)
        xs.add(cx)
    if not yrep:
        cy = tuple((e.y, e.dy) for e in moons)
        if cy in ys:
            yrep = len(ys)
        ys.add(cy)
    if not zrep:
        cz = tuple((e.z, e.dz) for e in moons)
        if cz in zs:
            zrep = len(zs)
        zs.add(cz)
    if all([xrep, yrep, zrep]):
        break
    [e.uvel(moons).upos() for e in moons]
    [e.finalize() for e in moons]

print(lcm(lcm(xrep, yrep), zrep))
