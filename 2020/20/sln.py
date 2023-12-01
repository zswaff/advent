#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
import re
from collections import defaultdict


with open("inp.txt") as fin:
    ts = {int(f[0][4:-1]): f[1:] for f in [e.split("\n") for e in fin.read().strip().split("\n\n")]}


# part 1
def bine(l):
    if not isinstance(l, str):
        l = "".join(l)
    return int(l.replace(".", "0").replace("#", "1"), 2)


t2ex = {
    k: {
        (bine(e[0] for e in v[::-1]), 0, False),
        (bine(v[0]), 1, False),
        (bine(e[-1] for e in v), 2, False),
        (bine(v[-1][::-1]), 3, False),
        (bine(e[0] for e in v), 0, True),
        (bine(v[0][::-1]), 1, True),
        (bine(e[-1] for e in v[::-1]), 2, True),
        (bine(v[-1]), 3, True),
    }
    for k, v in ts.items()
}
t2e = {k: {e[0] for e in v} for k, v in t2ex.items()}

e2t = defaultdict(set)
for tile, edges in t2e.items():
    for edge in edges:
        e2t[edge].add(tile)
t2t = defaultdict(set)
for tile, edges in t2e.items():
    for edge in edges:
        t2t[tile] |= e2t[edge]
    t2t[tile] -= {tile}

crnrs = [k for k, v in t2t.items() if len(v) == 2]
print(math.prod(crnrs))


# part 2
def p(tile, rot, flip, pes=False, verbose=True, trim=False):
    if isinstance(tile, int):
        img = list(ts[tile])
    else:
        img = tile
    if trim:
        img = [e[1:-1] for e in img[1:-1]]
    for _ in range(rot):
        img = ["".join(img[i][-j - 1] for i in range(len(img))) for j in range(len(img[0]))]
    if flip:
        img = img[::-1]
    if pes:
        side = len(img)
        mlen = 3
        lm = str(bine(e[0] for e in img))
        um = str(bine(img[0]))
        rm = str(bine(e[-1] for e in img))
        dm = str(bine(img[-1]))
        for i in range(len(img)):
            if i == side // 2:
                img[i] = f"{lm:>{mlen}} {img[i]} {rm:<{mlen}}"
                continue
            img[i] = (" " * (mlen + 1)) + img[i] + (" " * (mlen + 1))
        side += mlen * 2 + 2
        img.insert(0, str(tile) + f"{um:^{side}}"[4:])
        img.append(f"{dm:^{side}}")
    if verbose:
        print("\n".join(img))
    return img


def pr(l, pes=False, verbose=True, sep=" ", trim=False):
    r = p(*l[0], pes=pes, verbose=False, trim=trim)
    for t in l[1:]:
        img = p(*t, pes=pes, verbose=False, trim=trim)
        r = [f"{e}{sep}{f}" for e, f in zip(r, img)]
    if verbose:
        print("\n".join(r))
    return r


def pf(m, pes=False, verbose=True, trim=False):
    sep = " " if verbose else ""
    mnx, mxx = min(e[0] for e in m.keys()), max(e[0] for e in m.keys())
    mny, mxy = min(e[1] for e in m.keys()), max(e[1] for e in m.keys())
    r = []
    for y in range(mny, mxy + 1):
        l = []
        for x in range(mnx, mxx + 1):
            l.append(m[(x, y)])
        r += pr(l, pes=pes, verbose=False, sep=sep, trim=trim)
        if verbose:
            r.append("")
    if verbose:
        print("\n".join(r))
    return r


pano = {}
c1 = crnrs[0]
rots = []
for bval, rot, flip in t2ex[c1]:
    if flip:
        continue
    if len(e2t[bval]) == 1:
        rots.append(rot)
rot = {(0, 1): 0, (1, 2): 1, (2, 3): 2, (0, 3): 3}[tuple(sorted(rots))]
pano[(0, 0)] = c1, rot, False


def right(tile, rot, flip):
    nrot = (rot + 2) % 4
    return [b for b, r, f in t2ex[tile] if r == nrot and f == flip][0]


side = int(len(ts) ** 0.5)
for x in range(1, side):
    pt = pano[(x - 1, 0)]
    ne = right(*pt)
    ntile = list(e2t[ne] - {pt[0]})[0]
    nrot, nflip = [(r, f) for b, r, f in t2ex[ntile] if b == ne][0]
    pano[(x, 0)] = ntile, nrot, not nflip


def down(tile, rot, flip):
    nrot = (rot + (1 if flip else 3)) % 4
    return [b for b, r, f in t2ex[tile] if r == nrot and f == flip][0]


for y in range(1, side):
    for x in range(side):
        pt = pano[(x, y - 1)]
        ne = down(*pt)
        ntile = list(e2t[ne] - {pt[0]})[0]
        nrot, nflip = [(r, f) for b, r, f in t2ex[ntile] if b == ne][0]
        pano[(x, y)] = ntile, (nrot + (3 if nflip else 1)) % 4, not nflip
img = pf(pano, verbose=False, trim=True)

dragon = (
    """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""[
        1:-1
    ]
    .replace(" ", ".")
    .split("\n")
)
dlines = [re.compile(f"(?=({e}))") for e in dragon]
mn = math.inf
for rot in range(4):
    for flip in [True, False]:
        nimg = p(img, rot, flip, verbose=False)
        ons = [[f == "#" for f in e] for e in nimg]
        for i in range(len(img) - 2):
            starts = {e.start() for e in dlines[0].finditer(nimg[i])}
            starts &= {e.start() for e in dlines[1].finditer(nimg[i + 1])}
            starts &= {e.start() for e in dlines[2].finditer(nimg[i + 2])}
            for j in starts:
                for k in range(3):
                    for l, c in enumerate(dragon[k]):
                        if c == ".":
                            continue
                        ons[i + k][j + l] = False
        mn = min(mn, sum(sum(e) for e in ons))
print(mn)
