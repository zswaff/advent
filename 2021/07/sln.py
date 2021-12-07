#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


ns = [int(e) for e in dt.split(',')]
mx = max(ns)


# part 1
sm(min(sum(abs(f - e) for f in ns) for e in range(0, mx + 1)))


# part 2
def t(n):
    return (n * (n + 1)) // 2


sm(min(sum(t(abs(f - e)) for f in ns) for e in range(0, mx + 1)))
