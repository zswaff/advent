#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import deque


with open('inp.txt') as fin:
    od1, od2 = [
        [int(f) for f in e.split('\n')[1:]]
        for e in fin.read().strip().split('\n\n')
    ]


# part 1
d1, d2 = deque(od1), deque(od2)
while len(d1) != 0 and len(d2) != 0:
    c1, c2 = d1.popleft(), d2.popleft()
    if c1 > c2:
        d1.append(c1)
        d1.append(c2)
    else:
        d2.append(c2)
        d2.append(c1)
d = d1 if len(d2) == 0 else d2
print(sum(i * e for i, e in enumerate(reversed(d), 1)))


# part 2
def rec(d1, d2):
    states = set()
    while len(d1) != 0 and len(d2) != 0:
        state = tuple(d1), tuple(d2)
        if state in states:
            return True, d1
        states.add(state)
        c1, c2 = d1.popleft(), d2.popleft()
        if c1 <= len(d1) and c2 <= len(d2):
            won = rec(
                deque(d1[e] for e in range(c1)),
                deque(d2[e] for e in range(c2))
            )[0]
        else:
            won = c1 > c2
        if won:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)
    won = len(d2) == 0
    return won, d1 if won else d2

_, d = rec(deque(od1), deque(od2))
print(sum(i * e for i, e in enumerate(reversed(d), 1)))