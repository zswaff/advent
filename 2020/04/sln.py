#!/usr/bin/env python3
# -*- coding: utf-8 -*-


DIGITS = {str(e) for e in range(10)}
HEX_DIGITS = {hex(e)[2:] for e in range(16)}
EYES = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
RQMTS = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193)
    or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: len(x) == 7 and x[0] == "#" and set(x[1:]) <= HEX_DIGITS,
    "ecl": lambda x: x in EYES,
    "pid": lambda x: len(x) == 9 and set(x) <= DIGITS,
}


with open("inp.txt") as fin:
    inp = fin.read()


# part 1
ps = inp.split("\n\n")
c = 0
for p in ps:
    p = p.replace("\n", " ")
    es = p.split(" ")
    d = {k: v for k, v in [e.split(":") for e in es]}
    if d.keys() >= RQMTS.keys():
        c += 1
print(c)


# part 2
ps = inp.split("\n\n")
c = 0
for p in ps:
    p = p.replace("\n", " ")
    es = p.split(" ")
    d = {k: v for k, v in [e.split(":") for e in es]}
    if d.keys() >= RQMTS.keys():
        if all(v(d[k]) for k, v in RQMTS.items()):
            c += 1
print(c)
