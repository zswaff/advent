#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from web import *


# part 1
ns = [int(e) for e in ls]
sm(sum(ns[i+1] > e for i, e in enumerate(ns[:-1])))


# part 2
ns2 = [e + ns[i+1] + ns[i+2] for i, e in enumerate(ns[:-2])]
sm(sum(ns2[i+1] > e for i, e in enumerate(ns2[:-1])))
