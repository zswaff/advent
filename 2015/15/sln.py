#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


FMT = r'[A-Za-z]+: (?P<content>.*)'


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
ingrs = []
for line in lines:
    match = re.match(FMT, line).groupdict()
    ingrs.append(eval('{\'' + match['content'].replace(', ', ',\'').replace(' ', '\':') + '}'))


# part 1
m = 0
for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            l = 100 - i - j - k
            idxs = [i, j, k, l]
            r = 1
            for e in ['capacity', 'durability', 'flavor', 'texture']:
                c = sum(f[e] * g for f, g in zip(ingrs, idxs))
                if c <= 0:
                    r = 0
                    break
                r *= c
            m = max(m, r)
print(m)


# part 2
m = 0
for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            l = 100 - i - j - k
            idxs = [i, j, k, l]
            if sum(f['calories'] * g for f, g in zip(ingrs, idxs)) != 500:
                continue
            r = 1
            for e in ['capacity', 'durability', 'flavor', 'texture']:
                c = sum(f[e] * g for f, g in zip(ingrs, idxs))
                if c <= 0:
                    r = 0
                    break
                r *= c
            m = max(m, r)
print(m)
