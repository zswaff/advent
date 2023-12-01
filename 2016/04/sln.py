#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]

rooms = []
for l in lines:
    pref, chksm = l[:-1].split("[")
    splt = pref.split("-")
    rooms.append((splt[:-1], int(splt[-1]), chksm))


# part 1
c = 0
for names, code, chksm in rooms:
    ltrs = sorted((-v, k) for k, v in Counter("".join(names)).items())
    pchksm = "".join(e[1] for e in ltrs[:5])
    if pchksm == chksm:
        c += code
print(c)


# part 2
LTRS = {chr(ord("a") + i): i for i in range(26)}
SEARCH = "northpole"

for names, code, chksm in rooms:
    ltrs = sorted((-v, k) for k, v in Counter("".join(names)).items())
    pchksm = "".join(e[1] for e in ltrs[:5])
    if pchksm != chksm:
        continue
    name = " ".join(names).lower()
    dec = ""
    for c in name:
        if c == " ":
            dec += c
            continue
        dec += chr(ord("a") + ((LTRS[c] + code) % 26))
    if SEARCH in dec:
        print(code)
