#!/usr/bin/env python3
# -*- coding: utf-8 -*-


INP = 284573961


# part 1
l = str(INP)
for i in range(10):
    c = int(l[0])
    p = l[1:4]
    l = l[0] + l[4:]
    for j in range(1, 5):
        t = str((c - j - 1) % 9 + 1)
        if t in l:
            ti = l.index(t)
            l = l[:ti+1] + p + l[ti+1:]
            break
    l = l[1:] + l[0]
print(''.join(l + l).split('1')[1])


# part 2
class Node:
    def __init__(self, v, n):
        self.v = v
        self.n = n

cv = int(str(INP)[0])
curr = Node(cv, None)
ref = {cv: curr}
for i in [int(e) for e in list(str(INP))] + list(range(10, 1000001)):
    curr.n = Node(i, None)
    curr = curr.n
    ref[i] = curr
curr.n = ref[cv]
curr = curr.n

for i in range(10000000):
    c = curr.v
    p1 = curr.n
    p2 = p1.n
    p3 = p2.n
    ps = {p1.v, p2.v, p3.v}
    curr.n = p3.n
    for j in range(1, 5):
        t = (c - j - 1) % 1000000 + 1
        if t in ps:
            continue
        targ = ref[t]
        p3.n = targ.n
        targ.n = p1
        break
    curr = curr.n

print(ref[1].n.v * ref[1].n.n.v)
