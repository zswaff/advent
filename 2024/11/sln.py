#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
x = [int(e) for e in dt.split()]
for i in range(25):
    nx = []
    for e in x:
        if e == 0:
            nx.append(1)
            continue
        es = str(e)
        les = len(es)
        if les % 2 == 0:
            les2 = les // 2
            nx += [int(es[:les2]), int(es[les2:])]
            continue
        nx.append(e * 2024)
    x = nx
sm(len(x))


# part 2
x = Counter(int(e) for e in dt.split())
for i in range(75):
    nx = defaultdict(int)
    for e, v in x.items():
        if e == 0:
            nx[1] += v
            continue
        es = str(e)
        les = len(es)
        if les % 2 == 0:
            les2 = les // 2
            nx[int(es[:les2])] += v
            nx[int(es[les2:])] += v
            continue
        nx[e * 2024] += v
    x = nx
sm(sum(x.values()))
