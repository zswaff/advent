#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import re
from collections import defaultdict
from itertools import count


FMT = r'(?P<in>.*) => (?P<outq>\d+) (?P<outt>[A-Z]+)'

with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
rxns = {}
for line in lines:
    match = re.match(FMT, line).groupdict()
    rxns[match['outt']] = int(match['outq']), [(int(e.split(' ')[0]), e.split(' ')[1]) for e in match['in'].split(', ')]


# part 1
req = defaultdict(int, {'FUEL': 1})
while True:
    nxt = [(k, v) for k, v in req.items() if v > 0 and k != 'ORE']
    if len(nxt) == 0:
        break
    t, q = nxt[0]
    rq, rin = rxns[t]
    its = math.ceil(q / rq)
    req[t] -= rq * its
    for iq, it in rin:
        req[it] += iq * its
print(req['ORE'])


# part 2
req = defaultdict(int)
i = 0
for i in count():
    req['FUEL'] = 1
    while True:
        nxt = [(k, v) for k, v in req.items() if v > 0 and k != 'ORE']
        if len(nxt) == 0:
            break
        t, q = nxt[0]
        rq, rin = rxns[t]
        its = math.ceil(q / rq)
        req[t] -= rq * its
        for iq, it in rin:
            req[it] += iq * its
    if req['ORE'] > 10 ** 12:
        break
print(i)
