#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
O = list(reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]))


def ranks(cards):
    res = tuple(O.index(e) for e in cards)
    st = Counter(cards)
    if len(st) == 1:
        return 5, res
    if len(st) == 2:
        if 4 in st.values():
            return 4, res
        return 3, res
    if len(st) == 3:
        if 3 in st.values():
            return 2, res
        return 1, res
    if len(st) == 4:
        return 0, res
    return -1, res


hs = [e.strip().split(" ") for e in ls]
sm(
    sum(
        int(e[1]) * i
        for i, e in enumerate(sorted(hs, key=lambda x: (ranks(x[0]), x[1])), 1)
    )
)


# part 2
O = list(reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]))


def ranks(cards):
    res = tuple(O.index(e) for e in cards)
    st = Counter(cards)
    js = st.pop("J", 0)
    if js == 5:
        return 5, res
    st[st.most_common(1)[0][0]] += js
    if len(st) == 1:
        return 5, res
    if len(st) == 2:
        if 4 in st.values():
            return 4, res
        return 3, res
    if len(st) == 3:
        if 3 in st.values():
            return 2, res
        return 1, res
    if len(st) == 4:
        return 0, res
    return -1, res


sm(
    sum(
        int(e[1]) * i
        for i, e in enumerate(sorted(hs, key=lambda x: (ranks(x[0]), x[1])), 1)
    )
)
