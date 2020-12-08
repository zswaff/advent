#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


PATTERN = r'(?P<prefix>.*?)\((?P<count>\d*)x(?P<reps>\d*)\)(?P<rest>.*)'


with open('inp.txt') as fin:
    line = fin.read().strip()

# line = 'A(1x5)BC'


# part 1
def decompress(s):
    curr = s
    res = ''
    while (match := re.match(PATTERN, curr)) is not None:
        match_dict = match.groupdict()
        prefix, rest = match_dict['prefix'], match_dict['rest']
        count, reps = int(match_dict['count']), int(match_dict['reps'])
        res += prefix + (rest[:count] * reps)
        curr = rest[count:]
    return res + curr

print(len(decompress(line)))


# part 2
def rec(s):
    curr = s
    tot = 0
    while (match := re.match(PATTERN, curr)) is not None:
        match_dict = match.groupdict()
        prefix, rest = match_dict['prefix'], match_dict['rest']
        count, reps = int(match_dict['count']), int(match_dict['reps'])
        tot += len(prefix) + (rec(rest[:count]) * reps)
        curr = rest[count:]
    return tot + len(curr)

print(rec(line))
