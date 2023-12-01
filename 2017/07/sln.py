#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]


programs = []
parents = {}
children = {}
weights = {}
for line in lines:
    spl = line.split(" ")
    program = spl[0]
    programs.append(program)
    weight = int(spl[1][1:-1])
    weights[program] = weight
    arspl = line.split(" -> ")
    if len(arspl) == 1:
        continue
    kids = arspl[1].split(", ")
    children[program] = kids
    for kid in kids:
        parents[kid] = program


# part 1
root = list(set(programs) - set(parents.keys()))[0]
print(root)


# part 2
def balance_rcsv(node):
    cws = {c: balance_rcsv(c) for c in children.get(node, [])}
    ccws = Counter(cws.values())
    if len(ccws) > 1:
        gw, bw = [e[0] for e in ccws.most_common()]
        bad = next(k for k, v in cws.items() if v == bw)
        print(gw - bw + weights[bad])
        cws[bad] = gw
    return weights[node] + sum(cws.values())


balance_rcsv(root)
