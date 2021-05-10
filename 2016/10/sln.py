#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import re
from collections import defaultdict


VALUE_PAT = r'value (?P<val>\d*) goes to (?P<bot>bot \d*)'
GIVES_PAT = r'(?P<source>bot \d*) gives low to (?P<dest_lo>(bot|output) \d*) and high to (?P<dest_hi>(bot|output) \d*)'


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]

vals = defaultdict(list)
dests = {}
for line in lines:
    if (match := re.match(VALUE_PAT, line)) is not None:
        match_dict = match.groupdict()
        bot, value = match_dict['bot'], int(match_dict['val'])
        vals[bot].append(value)
        continue
    match_dict = re.match(GIVES_PAT, line).groupdict()
    source = match_dict['source']
    dest_lo, dest_hi = match_dict['dest_lo'], match_dict['dest_hi']
    dests[source] = dest_lo, dest_hi

q = [k for k, v in vals.items() if len(v) == 2]
while q:
    curr = q.pop(0)
    lo, hi = sorted(vals[curr])
    dest_lo, dest_hi = dests[curr]
    vals[dest_lo].append(lo)
    if len(vals[dest_lo]) == 2:
        q.append(dest_lo)
    vals[dest_hi].append(hi)
    if len(vals[dest_hi]) == 2:
        q.append(dest_hi)


# part 1
print([k for k, v in vals.items() if sorted(v) == [17, 61]][0][4:])


# part 2
print(math.prod(
    v[0]
    for k, v in vals.items()
    if k in {'output 0', 'output 1', 'output 2'}
))
