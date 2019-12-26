#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
from collections import defaultdict
from itertools import permutations


FMT = r'(?P<n1>[A-Za-z]+) would (?P<feel>lose|gain) (?P<e>\d+) happiness units by sitting next to (?P<n2>[A-Za-z]+).'


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
nodes = set()
edges = defaultdict(dict)
for line in lines:
    match = re.match(FMT, line).groupdict()
    n1, n2, amt, feel = match['n1'], match['n2'], int(match['e']), match['feel']
    if feel == 'lose':
        amt *= -1
    nodes |= {n1, n2}
    edges[n1][n2] = amt


# part 1
without = 0
for perm in permutations(nodes):
    c = 0
    for i, n1 in enumerate(perm):
        n2 = perm[(i + 1) % len(perm)]
        c += edges[n1][n2] + edges[n2][n1]
    without = max(without, c)
print(without)


# part 2
m = 0
for perm in permutations(nodes):
    c = 0
    for i, n1 in enumerate(perm[:-1]):
        n2 = perm[i + 1]
        c += edges[n1][n2] + edges[n2][n1]
    m = max(m, c)
print(m)
