#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


# part 1
g = set()
for l in ls:
    cns, rng = l.split(", ")
    cns = int(cns[2:])
    rngmn, rngmx = (int(e) for e in rng[2:].split(".."))
    if l[0] == "x":
        g |= {(cns, y) for y in range(rngmn, rngmx + 1)}
    else:
        g |= {(x, cns) for x in range(rngmn, rngmx + 1)}
ymn = min(e[1] for e in g)
ymx = max(e[1] for e in g)


vis = {(500, 0)}


def p():
    print(sum(ymn <= e[1] for e in vis))
    xmn = min(e[0] for e in g)
    xmx = max(e[0] for e in g)
    for y in range(ymx + 2):
        for x in range(xmn - 2, xmx + 3):
            if (x, y) in g:
                print("#", end="")
                continue
            if (x, y) in vis:
                print("~", end="")
                continue
            print(".", end="")
        print()
    print("-" * 50)


sq = [(500, 0)]
while sq:
    sx, sy = sl = sq.pop(0)
    if sl != (500, 0) and not (sx - 1, sy + 1) in g and not (sx + 1, sy + 1) in g:
        vis.remove(sl)
        continue
    for ny in count(sy + 1):
        nl = sx, ny
        if nl in g or ny > ymx:
            break
        vis.add(nl)
    if ny > ymx:
        continue
    ny -= 1
    for ly in count(ny, -1):
        walls = True
        for nx in count(sx + 1):
            nl = nx, ly
            if nl in g:
                break
            vis.add(nl)
            ul = nx, ly + 1
            if ul not in g and ul not in vis:
                walls = False
                if nl not in sq:
                    sq.append(nl)
                break
        for nx in count(sx - 1, -1):
            nl = nx, ly
            if nl in g:
                break
            vis.add(nl)
            ul = nx, ly + 1
            if ul not in g and ul not in vis:
                walls = False
                if nl not in sq:
                    sq.append(nl)
                break
        if not walls:
            break

mvis = set()
for vx, vy in vis:
    for my in count(vy - 1, -1):
        if (vx, my) not in vis and (vx + 1, my) in vis and (vx - 1, my) in vis:
            mvis.add((vx, my))
        else:
            break
vis |= mvis
sm(sum(ymn <= e[1] for e in vis))


# part 2
def check(vx, vy):
    for ny in count(vy + 1):
        if (vx, ny) not in vis:
            if (vx, ny) not in g:
                return False
            break
    for nx in count(vx + 1):
        if (nx, vy) not in vis:
            if (nx, vy) not in g:
                return False
            break
    for nx in count(vx - 1, -1):
        if (nx, vy) not in vis:
            if (nx, vy) not in g:
                return False
            break
    return True


sm(sum(check(*e) for e in vis))
