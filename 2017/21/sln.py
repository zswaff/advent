#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np


START = '.#./..#/###'


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]

def sta(s):
    return tuple(tuple(f == '#' for f in e) for e in s.split('/'))

def ntt(n):
    return tuple(tuple(e) for e in n)

def nts(n):
    return '\n'.join(''.join('#' if f else '.' for f in e) for e in n)

d = {}
for line in lines:
    cina, outt = [sta(e) for e in line.split(' => ')]
    outn = np.array(outt)
    for _ in range(2):
        for _ in range(4):
            d[cina] = outn
            cina = tuple(
                tuple(cina[i][-j - 1] for i in range(len(cina)))
                for j in range(len(cina[0]))
            )
        cina = tuple(reversed(cina))

# part 1
arr = np.array(sta(START))
for _ in range(5):
    s = 2 if len(arr) % 2 == 0 else 3
    arr = np.concatenate([
        np.concatenate([
            d[ntt(arr[y:y+s,x:x+s])] for x in range(0, len(arr), s)
        ], 1)
        for y in range(0, len(arr), s)
    ])
print(arr.sum())


# part 2
arr = np.array(sta(START))
for _ in range(18):
    s = 2 if len(arr) % 2 == 0 else 3
    arr = np.concatenate([
        np.concatenate([
            d[ntt(arr[y:y+s,x:x+s])] for x in range(0, len(arr), s)
        ], 1)
        for y in range(0, len(arr), s)
    ])
print(arr.sum())
