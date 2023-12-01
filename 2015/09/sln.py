#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import re
from collections import defaultdict


FMT = r"(?P<n1>[A-Za-z]+) to (?P<n2>[A-Za-z]*) = (?P<dist>\d+)"


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]
nodes = set()
edges = defaultdict(dict)
for line in lines:
    route = re.match(FMT, line).groupdict()
    d, n1, n2 = int(route["dist"]), route["n1"], route["n2"]
    nodes |= {n1, n2}
    edges[n1][n2] = d
    edges[n2][n1] = d


# part 1
def dfs(n1, searched):
    if len(searched) == len(nodes):
        return 0
    res = math.inf
    for n2, d in edges[n1].items():
        if n2 in searched:
            continue
        res = min(res, d + dfs(n2, searched | {n2}))
    return res


print(min(dfs(e, {e}) for e in nodes))


# part 2
def dfs(n1, searched):
    if len(searched) == len(nodes):
        return 0
    res = -math.inf
    for n2, d in edges[n1].items():
        if n2 in searched:
            continue
        res = max(res, d + dfs(n2, searched | {n2}))
    return res


print(max(dfs(e, {e}) for e in nodes))
