#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
sm(max(sum(int(f) for f in e) for e in ss))


# part 2
sm(sum(sorted(sum(int(f) for f in e) for e in ss)[-3:]))
