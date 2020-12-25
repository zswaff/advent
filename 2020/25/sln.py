#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


CARD = 3248366
DOOR = 4738476


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
cn = 7
for i in count(2):
    cn = (cn * 7) % 20201227
    if cn == CARD:
        break
print(pow(DOOR, i, 20201227))
