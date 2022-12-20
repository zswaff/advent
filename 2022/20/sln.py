#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


class Node:
    def __init__(self, data, old=None):
        self.data = data
        self.old = data if old is None else old
        self.next = None
        self.prev = None


def p(q):
    vis1 = set()
    curr = q[0]
    while curr not in vis1:
        vis1.add(curr)
        curr = curr.prev
    assert curr == q[0]
    vis2 = set()
    lst = []
    curr = q[0]
    while curr not in vis2:
        vis2.add(curr)
        lst.append(curr.data)
        curr = curr.next
    assert curr == q[0]
    assert vis1 == vis2
    assert len(vis1) == len(q)
    return lst


# part 1
ln = len(ls) - 1
q = [Node(e % ln, e) for e in [int(l) for l in ls]]
for i, e in enumerate(q):
    e.next = q[(i + 1) % len(q)]
    e.prev = q[(i - 1) % len(q)]
for n in q:
    if n.data == 0:
        continue
    n.prev.next = n.next
    n.next.prev = n.prev
    curr = n
    for i in range(n.data):
        curr = curr.next
    n.prev = curr
    n.next = curr.next
    curr.next.prev = n
    curr.next = n
c = 0
curr = q[0]
while curr.data != 0:
    curr = curr.next
for i in range(1, 3001):
    curr = curr.next
    if i % 1000 == 0:
        c += curr.old
sm(c)


# part 2
ln = len(ls) - 1
q = [Node(e % ln, e) for e in [int(l) * 811589153 for l in ls]]
# q = [Node((int(e) * 811589153) % ln, int(e)) for e in ls]
# q = [Node((int(e) * 811589153) % len(ls)) for e in ls]
for i, e in enumerate(q):
    e.next = q[(i + 1) % len(q)]
    e.prev = q[(i - 1) % len(q)]
for _ in range(10):
    for n in q:
        if n.data == 0:
            continue
        n.prev.next = n.next
        n.next.prev = n.prev
        curr = n
        for i in range(n.data):
            curr = curr.next
        n.prev = curr
        n.next = curr.next
        curr.next.prev = n
        curr.next = n
c = 0
curr = q[0]
while curr.data != 0:
    curr = curr.next
for i in range(1, 3001):
    curr = curr.next
    if i % 1000 == 0:
        c += curr.old
sm(c)
