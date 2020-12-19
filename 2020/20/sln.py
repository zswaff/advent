#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
from functools import lru_cache


with open('inp.txt') as fin:
    rule_str, line_str = fin.read().strip().split('\n\n')

rules = {
    k: [g.split() for g in v.split(' | ')]
    for k, v in [e.split(': ') for e in rule_str.split('\n')]
}
lines = line_str.split('\n')


@lru_cache
def gre(idx):
    if not idx.isnumeric():
        return idx.strip('"')
    r = '|'.join(''.join(gre(f) for f in e) for e in rules[idx])
    return r if r.isalpha() else f'({r})'


# part 1
matcher = re.compile(gre('0'))
print(sum(matcher.fullmatch(e) is not None for e in lines))


# part 2
_42 = gre('42')
_8 = f'{_42}+'
_31 = gre('31')
_11 = '(' + '|'.join(f'{_42}{{{i}}}{_31}{{{i}}}' for i in range(1, 9)) + ')'
matcher = re.compile(_8 + _11)
print(sum(matcher.fullmatch(e) is not None for e in lines))
