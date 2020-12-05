#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
from itertools import combinations


with open('inp.txt') as fin:
    weights = [int(e.strip()) for e in fin.readlines()]


# part 1
third  = sum(weights) // 3

best = math.inf, math.inf
def rec(len_a, sum_a, prod_a, sum_b, weights_a, weights_other):
    global best

    if sum_a > third or sum_b > third:
        return

    if len_a > best[0] or (len_a == best[0] and prod_a > best[1]):
        return

    if sum_a == sum_b == third:
        best = len_a, prod_a

    if sum_a < third:
        for i, e in enumerate(weights_a):
            rec(
                len_a + 1, sum_a + e, prod_a * e, sum_b, weights_a[i + 1:],
                weights_other + weights_a[:i])
        return
    n_weights_other = weights_a + weights_other
    for i, e in enumerate(n_weights_other):
        rec(len_a, sum_a, prod_a, sum_b + e, [], n_weights_other[i + 1:])

rec(0, 0, 1, 0, weights, [])
print(best[1])


# part 2
fourth  = sum(weights) // 4


def splittable(sum_b, sum_c, weights_b, weights_other_2):
    if sum_b == sum_c == fourth:
        return True

    if sum_b > fourth or sum_c > fourth:
        return False

    if sum_b < fourth:
        for i, e in enumerate(weights_b):
            if splittable(sum_b + e, sum_c, weights_b[i + 1:],
                weights_other_2 + weights_b[:i]):
                return True
        return False

    n_weights_other = weights_b + weights_other_2
    for i, e in enumerate(n_weights_other):
        if splittable(sum_b, sum_c + e, [], n_weights_other[i + 1:]):
            return True
    return False


for i in range(1, len(weights)):
    combs = [e for e in combinations(weights, i) if sum(e) == fourth]
    best = math.inf
    for comb in combs:
        rem = sorted(list(set(weights) - set(comb)))
        if splittable(0, 0, rem, []):
            best = min(best, math.prod(comb))
    if best != math.inf:
        print(best)
        break
