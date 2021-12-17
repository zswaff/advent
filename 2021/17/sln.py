#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


_, xs, ys = dt.split('=')
tx1, tx2 = [int(e) for e in xs[:-3].split('..')]
ty2, ty1 = [int(e) for e in ys.split('..')]

gxs = []
c = 0
for i in range(50):
    c += i
    if c > tx2:
        break
    if c >= tx1:
        gxs.append(i)


# part 1
mxmxy = 0
for ly in range(1000):
    for lx in gxs:
        dx, dy = lx, ly
        x = y = mxy = 0
        while x <= tx2 and y >= ty2:
            if tx1 <= x <= tx2 and ty1 >= y >= ty2:
                mxmxy = max(mxmxy, mxy)
                break
            x += dx
            y += dy
            mxy = max(mxy, y)
            dx = dx - 1 if dx else 0
            dy -= 1
sm(mxmxy)


# part 2
c = 0
for ly in range(ty2, 1000):
    for lx in range(gxs[0], tx2 + 1):
        dx, dy = lx, ly
        x = y = mxy = 0
        while x <= tx2 and y >= ty2:
            if tx1 <= x <= tx2 and ty1 >= y >= ty2:
                c += 1
                break
            x += dx
            y += dy
            mxy = max(mxy, y)
            dx = dx - 1 if dx else 0
            dy -= 1
sm(c)
