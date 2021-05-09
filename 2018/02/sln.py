#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter

from web import *


# part 1
sa(sum(1 for e in ls if 2 in set(Counter(e).values())) *
      sum(1 for e in ls if 3 in set(Counter(e).values())))


# part 2
def fn():
    for i, e in enumerate(ls):
        for f in ls[i + 1:]:
            for j in range(len(e)):
                if e[:j] + e[j+1:] == f[:j] + f[j+1:]:
                    return e[:j] + e[j+1:]
sb(fn())
