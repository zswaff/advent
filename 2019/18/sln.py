#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import itertools
from heapq import heappush, heappop


class PQ:
    def __init__(self):
        self.__heap = []
        self.__dict = {}
        self.__count = itertools.count()

    def __remove(self, item):
        elem = self.__dict.pop(item)
        elem[-1] = None

    def push(self, item, priority):
        if item in self.__dict:
            if self.__dict[item][0] <= priority:
                return
            self.__remove(item)
        elem = [priority, next(self.__count), item]
        heappush(self.__heap, elem)
        self.__dict[item] = elem

    def pop(self):
        while self.__heap:
            priority, _, item = heappop(self.__heap)
            if item is not None:
                del self.__dict[item]
                return item, priority
        raise KeyError('PQ Empty')


STRTS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DIAGS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
NOT_KEYS = {'#', '.'}


def get_adj(g_orig, starts):
    g_pos = {}
    for pos, val in g_orig.items():
        if val == '#':
            continue
        x, y = pos
        g_pos[pos] = []
        for dx, dy in STRTS:
            n_pos = x + dx, y + dy
            if n_pos not in g_orig or g_orig[n_pos] == '#':
                continue
            g_pos[pos].append(n_pos)

    def get_nbors(pos):
        o_val = g_orig[pos]
        q = [(pos, 0)]
        visited = set()
        result = []
        while q:
            c_pos, c_dist = q.pop(0)
            c_val = g_orig[c_pos]
            if c_val != o_val and c_val not in NOT_KEYS:
                result.append((c_val, c_dist))
            visited.add(c_pos)
            if c_val != o_val and c_val.isupper():
                continue
            for n_pos in g_pos[c_pos]:
                if n_pos in visited:
                    continue
                q.append((n_pos, c_dist + 1))
        return result

    g_adj = {i: get_nbors(e) for i, e in enumerate(starts)}
    for pos, val in g_orig.items():
        if val in NOT_KEYS:
            continue
        g_adj[val] = get_nbors(pos)
    return g_adj


with open('inp.txt') as fin:
    lines = [e.strip() for e in fin.readlines()]
g_orig = {(x, y): e for y, row in enumerate(lines) for x, e in enumerate(row)}
start = [k for k, v in g_orig.items() if v == '@'][0]
g_orig[start] = '.'
goal = frozenset(e for e in g_orig.values() if e.islower())


# part 1
g_adj = get_adj(g_orig, [start])

pq = PQ()
pq.push((0, frozenset()), 0)
visited = set()
while True:
    c_state, c_dist = pq.pop()
    c_val, c_keys = c_state
    if c_keys == goal:
        print(c_dist)
        break
    visited.add(c_state)
    for n_val, n_delta in g_adj[c_val]:
        is_key = n_val.islower()
        if not is_key and n_val.lower() not in c_keys:
            continue
        n_keys = frozenset(c_keys | {n_val}) if is_key else c_keys
        n_state = n_val, n_keys
        if n_state in visited:
            continue
        pq.push(n_state, c_dist + n_delta)


# part 2
g_new = {k: v for k, v in g_orig.items()}
g_new[start] = '#'
g_new.update({(start[0] + dx, start[1] + dy): '#' for dx, dy in STRTS})
starts = [(start[0] + dx, start[1] + dy) for dx, dy in DIAGS]

g_adj = get_adj(g_new, starts)

pq = PQ()
pq.push(((0, 1, 2, 3), frozenset()), 0)
visited = set()
while True:
    c_state, c_dist = pq.pop()
    c_vals, c_keys = c_state
    if c_keys == goal:
        print(c_dist)
        break
    visited.add(c_state)
    for tup_ind, c_val in enumerate(c_vals):
        for n_val, n_delta in g_adj[c_val]:
            is_key = n_val.islower()
            if not is_key and n_val.lower() not in c_keys:
                continue
            n_vals = list(c_vals)
            n_vals[tup_ind] = n_val
            n_vals = tuple(n_vals)
            n_keys = frozenset(c_keys | {n_val}) if is_key else c_keys
            n_state = n_vals, n_keys
            if n_state in visited:
                continue
            pq.push(n_state, c_dist + n_delta)
