#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    lines = [e.strip().split(')') for e in fin.readlines()]
sat_cent = {e[1]: e[0] for e in lines}


# part 1
o_counts = {}
def get_count(sat):
    if sat in o_counts:
        return o_counts[sat]
    if sat not in sat_cent:
        o_count = 0
    else:
        o_count = 1 + get_count(sat_cent[sat])
    o_counts[sat] = o_count
    return o_count
for sat in sat_cent.keys():
    get_count(sat)
print(sum(o_counts.values()))


# part 2
def count_path(s1, s2):
    s1_pars = {s1: 0}
    s2_pars = {s2: 0}
    while True:
        if s1 in s2_pars:
            return s1_pars[s1] + s2_pars[s1]
        if s2 in s1_pars:
            return s1_pars[s2] + s2_pars[s2]
        if s1 in sat_cent:
            s1p = sat_cent[s1]
            s1_pars[s1p] = s1_pars[s1] + 1
            s1 = s1p
        if s2 in sat_cent:
            s2p = sat_cent[s2]
            s2_pars[s2p] = s2_pars[s2] + 1
            s2 = s2p

print(count_path('YOU', 'SAN') - 2)
