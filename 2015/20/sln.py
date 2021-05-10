#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict
from itertools import count


# part 1
def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )

for i in count(1):
    if sum(factors(i)) >= 2900000:
        print(i)
        break


# part 2
dc = defaultdict(int)
for i in count(1):
    for j in range(1, 51):
        dc[i * j] += i * 11
    if dc[i] >= 29000000:
        print(i)
        break
