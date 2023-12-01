#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    traps = [[e == "^" for e in fin.read().strip()]]
l = len(traps[0])


def run(adtl):
    for i in range(adtl):
        n = []
        for j in range(l):
            left = traps[-1][j - 1] if j > 0 else False
            cent = traps[-1][j]
            rght = traps[-1][j + 1] if j < l - 1 else False
            n.append(
                (left and cent and (not rght))
                or ((not left) and cent and rght)
                or (left and (not cent) and (not rght))
                or ((not left) and (not cent) and rght)
            )
        traps.append(n)


# part 1
run(39)
print((40 * l) - sum(sum(e) for e in traps))


# part 2
run(400000 - 40)
print((400000 * l) - sum(sum(e) for e in traps))
