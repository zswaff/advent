#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import cache

from common import *
from web import *


s, rs = dt.split("\n\n")
rs = dict([e.split(" -> ") for e in rs.split("\n")])


# part 1
st = Counter([s[i : i + 2] for i in range(len(s) - 1)])
for _ in range(10):
    nst = Counter()
    for k, v in st.items():
        nst[k[0] + rs[k]] += v
        nst[rs[k] + k[1]] += v
    st = nst
c = Counter({s[0]: 1, s[1]: 1})
for (k1, k2), v in st.items():
    c[k1] += v
    c[k2] += v
c = c.most_common()
sm((c[0][1] - c[-1][1]) // 2)


# part 2
st = Counter([s[i : i + 2] for i in range(len(s) - 1)])
for _ in range(40):
    nst = Counter()
    for k, v in st.items():
        nst[k[0] + rs[k]] += v
        nst[rs[k] + k[1]] += v
    st = nst
c = Counter({s[0]: 1, s[1]: 1})
for (k1, k2), v in st.items():
    c[k1] += v
    c[k2] += v
c = c.most_common()
sm((c[0][1] - c[-1][1]) // 2)
