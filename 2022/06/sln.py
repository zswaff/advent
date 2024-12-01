#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
sm(next(i for i in range(4, len(l) + 1) if len(set(list(l[i - 4 : i]))) == 4))


# part 2
sm(next(i for i in range(14, len(l) + 1) if len(set(list(l[i - 14 : i]))) == 14))
