#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open("inp.txt") as fin:
    ns = [int(e) for e in fin.read().strip()]


# part 1
print(sum(e for i, e in enumerate(ns) if e == ns[(i + 1) % len(ns)]))


# part 2
print(sum(e for i, e in enumerate(ns) if e == ns[(i + len(ns) // 2) % len(ns)]))
