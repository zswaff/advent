#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
def hsh(s):
    res = 0
    for f in s:
        res += ord(f)
        res *= 17
        res %= 256
    return res


sm(sum(hsh(e) for e in dt.split(",")))


# part 2
mp = defaultdict(list)
for l in dt.split(","):
    if l.endswith("-"):
        k = hsh(l[:-1])
        mp[k] = [f for f in mp[k] if f[0] != l[:-1]]
        continue
    e = l.split("=")
    k = hsh(e[0])
    for f in mp[k]:
        if f[0] != e[0]:
            continue
        f[1] = e[1]
        break
    else:
        mp[k].append(e)
sm(sum(sum((k + 1) * i * int(e[1]) for i, e in enumerate(v, 1)) for k, v in mp.items()))
