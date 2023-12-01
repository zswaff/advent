#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict

from comp import Comp


# part 1
def run():
    cs = [Comp(fname="inp.txt").add_inputs([i]) for i in range(50)]
    ms = defaultdict(list)
    while True:
        for i in range(50):
            m = [-1]
            if ms[i]:
                m = ms[i].pop(0)
            cs[i].add_inputs(m)
            o = cs[i].last_outputs
            for a, x, y in zip(o[::3], o[1::3], o[2::3]):
                if a == 255:
                    return y
                ms[a].append([x, y])


print(run())


# part 2
def run():
    cs = [Comp(fname="inp.txt").add_inputs([i]) for i in range(50)]
    ms = defaultdict(list)
    n = []
    ns = set()
    while True:
        na = True
        for i in range(50):
            m = [-1]
            if ms[i]:
                na = False
                m = ms[i].pop(0)
            cs[i].add_inputs(m)
            o = cs[i].last_outputs
            if o:
                na = False
            for a, x, y in zip(o[::3], o[1::3], o[2::3]):
                if a == 255:
                    n = [x, y]
                    continue
                ms[a].append([x, y])
        if na:
            y = n[1]
            if y in ns:
                return y
            ns.add(y)
            ms[0].append(n)


print(run())
