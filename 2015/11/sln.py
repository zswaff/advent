#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import count


# parts 1 and 2
pw = 'cqjxjnds'
idx = sum((ord(e) - ord('a')) * (26 ** i) for i, e in enumerate(reversed(pw)))
done = False
for i in count(idx):
    pw = ''.join([chr(ord('a') + ((i // (26 ** j)) % 26)) for j in range(7, -1, -1)])
    if not any(ord(pw[j]) + 2 == ord(pw[j + 1]) + 1 == ord(pw[j + 2]) for j in range(len(pw) - 2)):
        continue
    if set(pw) & set('ilo'):
        continue
    doubs = [j for j in range(len(pw) - 1) if pw[j] == pw[j+1]]
    if not doubs or min(doubs) + 2 > max(doubs):
        continue
    print(pw)
    if done:
        break
    done = True


# part 2

