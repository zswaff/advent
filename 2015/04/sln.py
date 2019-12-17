#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count
from hashlib import md5


# part 1
key = 'bgvyzdsv'
for i in count():
    h = md5(str.encode(key + str(i))).hexdigest()
    if h.startswith('00000'):
        print(i)
        break


# part 2
for i in count():
    h = md5(str.encode(key + str(i))).hexdigest()
    if h.startswith('000000'):
        print(i)
        break
