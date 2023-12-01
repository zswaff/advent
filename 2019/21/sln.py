#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from comp import Comp


SUBS = [(str(i), chr(i + ord("A") - 1)) for i in range(1, 10)] + [
    ("O", "J"),
    ("!", "NOT"),
    ("&", "AND"),
    ("|", "OR"),
]


# part 1
INS = ["| 1 O", "& 2 O", "& 3 O", "! O O", "& 4 O"]

for i in range(len(INS)):
    for k, v in SUBS:
        INS[i] = INS[i].replace(k, v)
trans = [ord(e) for e in "\n".join(INS + ["WALK", ""])]
res = Comp(fname="inp.txt").add_inputs(trans).outputs
print(res[-1])


# part 2
INS = ["| 1 O", "& 2 O", "& 3 O", "! O O", "& 4 O", "| 5 T", "| 8 T", "& T O"]

for i in range(len(INS)):
    for k, v in SUBS:
        INS[i] = INS[i].replace(k, v)
trans = [ord(e) for e in "\n".join(INS + ["RUN", ""])]
res = Comp(fname="inp.txt").add_inputs(trans).outputs
print(res[-1])
