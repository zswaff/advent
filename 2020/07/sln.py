#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
from collections import defaultdict


PATTERN = r'(?P<parent>.*) bags contain (?P<children>.*)\.'


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]


par_to_chil = {}
chil_to_par = defaultdict(list)
for l in lines:
    match_dict = re.match(PATTERN, l).groupdict()
    parent, children_str = match_dict['parent'], match_dict['children']
    if children_str == 'no other bags':
        par_to_chil[parent] = []
        continue
    children = []
    for child_str in children_str.split(', '):
        spl = child_str.split(' ')
        child = ' '.join(spl[1:-1])
        chil_to_par[child].append(parent)
        children.append((int(spl[0]), child))
    par_to_chil[parent] = children


start = 'shiny gold'


# part 1
q = [start]
visited = set()
while q:
    curr = q.pop(0)
    if curr in visited:
        continue
    visited.add(curr)
    q += chil_to_par[curr]
print(len(visited) - 1)


# part 2
cache = {}
def get_child_count(bag):
    if bag in cache:
        return cache[bag]
    val = 1 + sum(c * get_child_count(v) for c, v in par_to_chil[bag])
    cache[bag] = val
    return val


print(get_child_count(start) - 1)
