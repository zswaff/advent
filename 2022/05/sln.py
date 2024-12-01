#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *

# part 1
stacks, ops = ss
stacks = reversed(stacks[:-1])
ps = defaultdict(list)
for l in stacks:
    lp = list(l[1::4])
    for i, c in enumerate(lp, 1):
        if c == " ":
            continue
        ps[i].append(c)
for l in ops:
    n, s, d = pa(l, "move {i} from {i} to {i}")
    mv = ps[s][-n:]
    ps[s] = ps[s][:-n]
    ps[d] += reversed(mv)
sm("".join(ps[i][-1] for i in range(1, len(ps) + 1)))


# part 2
stacks, ops = ss
stacks = reversed(stacks[:-1])
ps = defaultdict(list)
for l in stacks:
    lp = list(l[1::4])
    for i, c in enumerate(lp, 1):
        if c == " ":
            continue
        ps[i].append(c)
for l in ops:
    n, s, d = pa(l, "move {i} from {i} to {i}")
    mv = ps[s][-n:]
    ps[s] = ps[s][:-n]
    ps[d] += mv
sm("".join(ps[i][-1] for i in range(1, len(ps) + 1)))
