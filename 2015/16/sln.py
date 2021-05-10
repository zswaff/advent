#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


FMT = r'Sue \d+: (?P<content>.*)'


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
sues = []
for line in lines:
    match = re.match(FMT, line).groupdict()
    sues.append(eval('{\'' + match['content'].replace(':', '\':').replace(', ', ', \'') + '}'))


# part 1
ref = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}
for i, e in enumerate(sues):
    if all(v == ref[k] for k, v in e.items()):
        print(i + 1)


# part 2
fref = {
    'children': lambda x: x == 3,
    'cats': lambda x: x > 7,
    'samoyeds': lambda x: x == 2,
    'pomeranians': lambda x: x < 3,
    'akitas': lambda x: x == 0,
    'vizslas': lambda x: x == 0,
    'goldfish': lambda x: x < 5,
    'trees': lambda x: x > 3,
    'cars': lambda x: x == 2,
    'perfumes': lambda x: x == 1
}
for i, e in enumerate(sues):
    if all(fref[k](v) for k, v in e.items()):
        print(i + 1)
