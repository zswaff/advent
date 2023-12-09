#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
c = 0
for l in ls:
    l = [int(e) for e in l.split()]
    st = []
    st.append(l)
    while True:
        nl = st[-1]
        nl = [e - nl[i - 1] for i, e in enumerate(nl[1:], 1)]
        if all(e == 0 for e in nl):
            break
        st.append(nl)
    st.reverse()
    x = 0
    for s in st:
        x = s[-1] + x
    c += x
sm(c)


# part 2
c = 0
for l in ls:
    l = [int(e) for e in l.split()]
    st = []
    st.append(l)
    while True:
        nl = st[-1]
        nl = [e - nl[i - 1] for i, e in enumerate(nl[1:], 1)]
        if all(e == 0 for e in nl):
            break
        st.append(nl)
    st.reverse()
    x = 0
    for s in st:
        x = s[0] - x
    c += x
sm(c)
