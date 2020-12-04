#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


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

best = math.inf, math.inf
def rec(len_a, sum_a, prod_a, sum_b, sum_c, weights_a, weights_b, weights_other):
    global best

    if sum_a > fourth or sum_b > fourth or sum_c > fourth:
        return

    if len_a > best[0] or (len_a == best[0] and prod_a > best[1]):
        return

    if sum_a == sum_b == sum_c == fourth:
        best = len_a, prod_a

    if sum_a < fourth:
        for i, e in enumerate(weights_a):
            rec(
                len_a + 1, sum_a + e, prod_a * e, sum_b, sum_c,
                weights_a[i + 1:], weights_b + weights_a[:i], [])
        return
    if sum_b < fourth:
        n_weights_b = weights_a + weights_b
        for i, e in enumerate(n_weights_b):
            rec(
                len_a, sum_a, prod_a, sum_b + e, sum_c, [],
                n_weights_b[i + 1:], weights_other + weights_other[:i])
    n_weights_other = weights_b + weights_other
    for i, e in enumerate(n_weights_other):
        rec(
            len_a, sum_a, prod_a, sum_b + e, sum_c, [], [],
            n_weights_other[i + 1:])

rec(0, 0, 1, 0, 0, weights, [], [])
print(best[1])
