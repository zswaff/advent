#!/usr/bin/env python3
# -*- coding: utf-8 -*-


DIRS = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0)
}


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
x = y = 1
res = ''
for l in lines:
    for c in l:
        dx, dy = DIRS[c]
        nx, ny = x + dx, y + dy
        if not (0 <= nx <= 2 and 0 <= ny <= 2):
            continue
        x, y = nx, ny
    res += str(1 + x + (y * 3))
print(res)


# part 2
keypad = """  1  
 234 
56789
 ABC 
  D  """
locs = {}
for y, row in enumerate(keypad.split('\n')):
    for x, c in enumerate(row):
        if c == ' ':
            continue
        locs[(x, y)] = c

x, y = 0, 2
res = ''
for l in lines:
    for c in l:
        dx, dy = DIRS[c]
        nx, ny = x + dx, y + dy
        if (nx, ny) in locs:
            x, y = nx, ny
    res += locs[(x, y)]
print(res)
