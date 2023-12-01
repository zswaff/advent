#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


INP = 289326


# part 1
c, i, n = INP - 1, 0, 0
for i in count(1):
    n = 8 * i
    if c > n:
        c -= n
    else:
        break
print(i + abs(((c - 1) % (i * 2)) - i + 1))


# part 2
def solve():
    g = {(0, 0): 1}
    x, y = 1, -1
    for i in count(2, 2):
        for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            for _ in range(i):
                x, y = x + dx, y + dy
                g[(x, y)] = sum(
                    g.get((x + ax, y + ay), 0) for ax in range(-1, 2) for ay in range(-1, 2)
                )
                if g[(x, y)] > INP:
                    return g[(x, y)]
        x, y = x + 1, y - 1


print(solve())
