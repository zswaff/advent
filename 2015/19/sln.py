#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


FMT = r'(?P<in>[A-Za-z]+) => (?P<out>[A-Za-z]+)'


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
tsns = []
for line in lines[:-2]:
    match = re.match(FMT, line).groupdict()
    tsns.append((match['in'], match['out']))


# part 1
r = set()
chem = lines[-1]
for ti, to in tsns:
    spl = chem.split(ti)
    for i in range(len(spl) - 1):
        r.add(ti.join(spl[:i + 1]) + to + ti.join(spl[i + 1:]))
print(len(r))


# part 2
tsns.sort(key=lambda x: len(x[1]))

r = {chem}
q = [(chem, 0)]
j = -1
while len(q) != 0:
    j += 1
    e, c = q.pop()
    if e == 'e':
        print(c)
        break
    for ti, to in tsns:
        spl = e.split(to)
        for i in range(len(spl) - 1):
            pot = to.join(spl[:i + 1]) + ti + to.join(spl[i + 1:])
            if pot in r:
                continue
            r.add(pot)
            q.append((pot, c + 1))
