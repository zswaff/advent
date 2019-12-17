#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from comp import Comp


DRS = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}


# part 1
loc = 0, 0
cmp = Comp(fin='inp.txt')
walls = {(0, 0): False}

def route(s, e):
    srd = {s}
    q = [(s, [])]
    while q:
        c, rt = q.pop(0)
        if c == e:
            return rt
        for dr, (dx, dy) in DRS.items():
            n = c[0] + dx, c[1] + dy
            if n in srd or walls.get(n, True):
                continue
            srd.add(n)
            q.append((n, [dr] + rt))
    return None

def search():
    global loc
    q = [loc]
    unit = None
    while q:
        c = q.pop()
        cmp.add_inputs(route(loc, c))
        loc = c
        for dr, (dx, dy) in DRS.items():
            n = loc[0] + dx, loc[1] + dy
            if n in walls:
                continue
            res = cmp.add_inputs([dr]).last_outputs[0]
            walls[n] = res == 0
            if res == 0:
                continue
            if res == 2:
                unit = n
            q += [loc, n]
            loc = n
            break
    return unit

unit = search()
print(len(route((0, 0), unit)))


# part 2
srd = {unit: 0}
q = [unit]
while q:
    c = q.pop(0)
    for dr, (dx, dy) in DRS.items():
        n = c[0] + dx, c[1] + dy
        if n in srd or walls.get(n, True):
            continue
        srd[n] = srd[c] + 1
        q.append(n)
print(max(e for e in srd.values()))
