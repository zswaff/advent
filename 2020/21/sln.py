#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    fds = [
        (set(f[0].split()), set(f[1].split(", ")))
        for f in [e.strip()[:-1].split(" (contains ") for e in fin.readlines()]
    ]
ingrs = set().union(*[f[0] for f in fds])
alrgns = set().union(*[f[1] for f in fds])


# part 1
mb_ingrs = set().union(
    *[(e := [f[0] for f in fds if g in f[1]])[0].intersection(*e[1:]) for g in alrgns]
)
print(sum(len(e[0] - mb_ingrs) for e in fds))


# part 2
b_ingrs = {e: set(mb_ingrs) for e in alrgns}
for ins, als in fds:
    for al in als:
        b_ingrs[al].intersection_update(ins)
while any(len(e) != 1 for e in b_ingrs.values()):
    for al, pins in b_ingrs.items():
        if len(pins) != 1:
            continue
        for al2 in b_ingrs.keys():
            if al2 == al:
                continue
            b_ingrs[al2] -= pins
print(",".join(list(e[1])[0] for e in sorted(b_ingrs.items())))
