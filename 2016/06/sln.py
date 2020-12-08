#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict, Counter


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


# part 1
cntrs = defaultdict(Counter)
for line in lines:
    for i, c in enumerate(line):
        cntrs[i][c] += 1
print(''.join(v.most_common()[0][0] for _, v in sorted(cntrs.items())))


# part 2
print(''.join(v.most_common()[-1][0] for _, v in sorted(cntrs.items())))
