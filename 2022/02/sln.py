#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *

O = {"A": 1, "B": 2, "C": 3}
S = {"X": 1, "Y": 2, "Z": 3}

# part 1
X = {
    (1, 1): 3,
    (1, 2): 6,
    (1, 3): 0,
    (2, 1): 0,
    (2, 2): 3,
    (2, 3): 6,
    (3, 1): 6,
    (3, 2): 0,
    (3, 3): 3,
}
c = 0
for l in ls:
    o, s = l.split(" ")
    ox, sx = O[o], S[s]
    c += sx + X[(ox, sx)]
sm(9241)


# part 2
scores = {"X": 0, "Y": 3, "Z": 6}
X = {
    (1, 1): 3,
    (1, 2): 1,
    (1, 3): 2,
    (2, 1): 1,
    (2, 2): 2,
    (2, 3): 3,
    (3, 1): 2,
    (3, 2): 3,
    (3, 3): 1,
}
c = 0
for l in ls:
    o, r = l.split(" ")
    ox, rx = O[o], S[r]
    c += X[(ox, rx)] + scores[r]
sm(c)
