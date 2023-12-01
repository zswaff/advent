#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count
from hashlib import md5


door_id = "abbhdwsy"


# part 1
pw = ""
for i in count():
    hsh = md5((door_id + str(i)).encode()).hexdigest()
    if hsh[:5] != "00000":
        continue
    pw += hsh[5]
    if len(pw) == 8:
        break
print(pw)


# part 2
pw = {}
for i in count():
    hsh = md5((door_id + str(i)).encode()).hexdigest()
    if hsh[:5] != "00000":
        continue
    idx, ch = hsh[5:7]
    if int(idx, 16) >= 8:
        continue
    if idx in pw:
        continue
    pw[idx] = ch
    if len(pw) == 8:
        break
print("".join(e[1] for e in sorted(pw.items())))
