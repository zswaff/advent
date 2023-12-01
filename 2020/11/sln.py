#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict


with open("inp.txt") as fin:
    seats = [[f == "L" for f in e.strip()] for e in fin.readlines()]


# part 1
def round1(occs):
    res = [[False for _ in e] for e in seats]
    for y, row in enumerate(seats):
        for x, is_seat in enumerate(row):
            if not is_seat:
                continue
            adj = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0:
                        continue
                    try:
                        if occs[ny][nx]:
                            adj += 1
                    except IndexError:
                        continue
            if adj == 0:
                res[y][x] = True
            elif adj >= 4:
                res[y][x] = False
            else:
                res[y][x] = occs[y][x]
    return res


state = [[False for _ in e] for e in seats]
while True:
    new = round1(state)
    if new == state:
        break
    state = new
print(sum(sum(e) for e in state))


# part 2
nbors = defaultdict(list)
for y, row in enumerate(seats):
    for x, is_seat in enumerate(row):
        if not is_seat:
            continue
        xt = False
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                nx, ny = x, y
                while True:
                    nx, ny = nx + dx, ny + dy
                    if nx < 0 or ny < 0:
                        break
                    try:
                        if seats[ny][nx]:
                            nbors[(x, y)].append((nx, ny))
                            break
                    except IndexError:
                        break


def round2(occs):
    res = [[False for _ in e] for e in seats]
    for y, row in enumerate(seats):
        for x, is_seat in enumerate(row):
            if not is_seat:
                continue
            adj = sum(occs[ny][nx] for nx, ny in nbors[(x, y)])
            if adj == 0:
                res[y][x] = True
            elif adj >= 5:
                res[y][x] = False
            else:
                res[y][x] = occs[y][x]
    return res


state = [[False for _ in e] for e in seats]
while True:
    new = round2(state)
    if new == state:
        break
    state = new
print(sum(sum(e) for e in state))
