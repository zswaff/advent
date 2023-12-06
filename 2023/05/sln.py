#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
seeds = [int(e) for e in ss[0][0][7:].split(" ")]
maps = [[[int(g) for g in e.split(" ")] for e in f[1:]] for f in ss[1:]]
r = inf
for seed in seeds:
    cval = seed
    for map in maps:
        for dst, src, len in map:
            if src <= cval < src + len:
                cval = dst + cval - src
                break
    r = min(r, cval)
sm(r)


# part 2
nmaps = []
for map in maps:
    nmap = []
    p_src_max = 0
    for dst, src, len in sorted(map, key=lambda e: e[1]):
        assert src >= p_src_max
        if src > p_src_max:
            nmap.append([p_src_max, p_src_max, src - p_src_max])
        nmap.append([dst, src, len])
        p_src_max = src + len
    nmap = [((src, src + len - 1), (dst, dst + len - 1)) for dst, src, len in nmap]
    nmaps.append(nmap)
mx = max(max(e[-1][0][1], e[-1][1][1]) for e in nmaps)
for nmap in nmaps:
    p_src_max = nmap[-1][0][1]
    if p_src_max < mx:
        nmap.append(((p_src_max + 1, mx), (p_src_max + 1, mx)))

fmap = nmaps.pop(0)
while nmaps:
    nmap = []
    cmap = nmaps.pop(0)
    for (o_src_min, o_src_max), (o_dst_min, o_dst_max) in fmap:
        for (n_src_min, n_src_max), (n_dst_min, n_dst_max) in cmap:
            if o_dst_min > n_src_max:
                continue
            n_min = max(o_dst_min, n_src_min)
            o_min_delta = n_min - o_dst_min
            n_min_delta = n_min - n_src_min
            n_max = min(o_dst_max, n_src_max)
            o_max_delta = o_dst_max - n_max
            n_max_delta = n_src_max - n_max
            nmap.append(
                (
                    (o_src_min + o_min_delta, o_src_max - o_max_delta),
                    (n_dst_min + n_min_delta, n_dst_max - n_max_delta),
                )
            )
            if o_dst_max <= n_src_max:
                break
    fmap = nmap

nseeds = sorted(zip(seeds[::2], seeds[1::2]))
r = inf
for seed_min, seed_len in nseeds:
    seed_max = seed_min + seed_len - 1
    for (src_min, src_max), (dst_min, dst_max) in fmap:
        if seed_min > src_max:
            continue
        n_min = max(seed_min, src_min)
        min_delta = n_min - src_min
        r = min(r, dst_min + min_delta)
        if seed_max <= src_max:
            break
sm(r)
