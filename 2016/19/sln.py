#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from queue import Queue


INP = 3001330


# part 1
q = Queue()
for i in range(1, INP + 1):
    q.put(i)
while q.qsize() > 1:
    q.put(q.get())
    q.get()
print(q.get())


# part 2
l = list(range(1, INP + 1))
i = 0
while len(l) > 1:
    idx = i + (len(l) // 2)
    if idx >= len(l):
        idx -= len(l)
        i -= 1
    l.pop(idx)
    i += 1
    if i >= len(l):
        i = 0
print(l[0])
