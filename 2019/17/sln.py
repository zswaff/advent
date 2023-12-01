#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from comp import Comp


# part 1
cmp = Comp(fin="inp.txt")
v = "".join(chr(e) for e in cmp.outputs).strip()
m = [list(f) for f in v.split("\n")]
print(
    sum(
        x * y
        for y, row in enumerate(m[1:-1], 1)
        for x, e in enumerate(row[1:-1], 1)
        if e == m[y + 1][x] == m[y - 1][x] == m[y][x + 1] == m[y][x - 1] == "#"
    )
)


# part 2
DIRS = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
CHRS = {"^": 0, ">": 1, "vis": 2, "<": 3}

sloc, sdr = None, None
n = {}
for y, row in enumerate(m):
    for x, e in enumerate(row):
        n[(x, y)] = e != "."
        if e in CHRS:
            sloc, sdr = (x, y), CHRS[e]

loc, dr = sloc, sdr
rt = []
while True:
    nloc = loc[0] + DIRS[dr][0], loc[1] + DIRS[dr][1]
    while n.get(nloc, False):
        rt[-1][1] += 1
        loc = nloc
        nloc = loc[0] + DIRS[dr][0], loc[1] + DIRS[dr][1]
    ndr = (dr - 1) % 4
    nloc = loc[0] + DIRS[ndr][0], loc[1] + DIRS[ndr][1]
    if n.get(nloc, False):
        rt.append(["L", 0])
        dr = ndr
        continue
    ndr = (dr + 1) % 4
    nloc = loc[0] + DIRS[ndr][0], loc[1] + DIRS[ndr][1]
    if n.get(nloc, False):
        rt.append(["R", 0])
        dr = ndr
        continue
    break

rt = [tuple(e) for e in rt]
rtm = {}
rts = []
for e in rt:
    if e not in rtm:
        rtm[e] = len(rtm)
    rts.append(rtm[e])
x = "".join(str(e) for e in rts)


def attempt(ls):
    s = x
    abc = [""] * 3
    r = []
    while len(s) != 0:
        for i, (l, e) in enumerate(zip(ls, abc)):
            if len(e) != l:
                abc[i] = e = s[:l]
            if s.startswith(e):
                s = s[l:]
                r.append(chr(ord("A") + i))
                break
        else:
            return None
    return r, list(abc[0]), list(abc[1]), list(abc[2])


def find():
    for al in range(1, 6):
        for bl in range(1, 6):
            for cl in range(1, 6):
                e = attempt([al, bl, cl])
                if e is not None:
                    return e
    return None


r = find()
m = r[0]
rrtm = {v: k for k, v in rtm.items()}
abc = [[g for f in e for g in rrtm[int(f)]] for e in r[1:]]
inp = [ord(g) for g in "\n".join(",".join(str(f) for f in e) for e in [m] + abc + [["n"], []])]

with open("inp.txt") as fin:
    ops = [int(e) for e in fin.read().strip().split(",")]
ops[0] = 2
cmp = Comp(ops=ops).add_inputs(inp)
print(cmp.outputs[-1])
