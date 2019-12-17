#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    lights = {
        (x, y): f == '#'
        for y, e in enumerate(fin.readlines())
        for x, f in enumerate(e.strip())
    }


# part 1
cl = lights
for i in range(100):
    nl = {}
    for x in range(100):
        for y in range(100):
            nbors = sum(cl.get((x + dx, y + dy), 0) for dx in range(-1, 2) for dy in range(-1, 2)) - cl[x, y]
            nl[(x, y)] = nbors == 3 or nbors + cl[x, y] == 3
    cl = nl
print(sum(cl.values()))


# part 2
cl = lights
lights[(0, 0)] = lights[(0, 99)] = lights[(99, 0)] = lights[(99, 99)] = True
for i in range(100):
    nl = {}
    for x in range(100):
        for y in range(100):
            nbors = sum(cl.get((x + dx, y + dy), 0) for dx in range(-1, 2) for dy in range(-1, 2)) - cl[x, y]
            nl[(x, y)] = nbors == 3 or nbors + cl[x, y] == 3 or (x in {0, 99} and y in {0, 99})
    cl = nl
print(sum(cl.values()))
