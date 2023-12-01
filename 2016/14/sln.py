#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict
from itertools import count, groupby
from hashlib import md5


INP = "yjdafjpo"


# part 1
res = []
pots = defaultdict(list)
for i in count():
    hsh = md5((INP + str(i)).encode()).hexdigest()
    trip = None
    for ch, group in groupby(hsh):
        l = len(list(group))
        if l >= 3 and trip is None:
            trip = ch
        if l >= 5:
            if ch not in pots:
                continue
            for j in pots.pop(ch):
                if j + 1000 >= i:
                    res.append(j)
            res.sort()
    if trip is not None:
        pots[trip].append(i)
    if len(res) >= 64 and res[63] + 1000 <= i:
        break
print(res[63])


# part 2
res = []
pots = defaultdict(list)
for i in count():
    hsh = md5((INP + str(i)).encode()).hexdigest()
    for j in range(2016):
        hsh = md5(hsh.encode()).hexdigest()
    trip = None
    for ch, group in groupby(hsh):
        l = len(list(group))
        if l >= 3 and trip is None:
            trip = ch
        if l >= 5:
            if ch not in pots:
                continue
            for j in pots.pop(ch):
                if j + 1000 >= i:
                    res.append(j)
            res.sort()
    if trip is not None:
        pots[trip].append(i)
    if len(res) >= 64 and res[63] + 1000 <= i:
        break
print(res[63])
