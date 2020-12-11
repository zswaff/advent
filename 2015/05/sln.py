#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter, defaultdict


with open('inp.txt') as fin:
    words = [e.strip() for e in fin.readlines()]


# part 1
def is_nice(word):
    c = Counter(word)
    if sum(c[e] for e in ['a', 'elvl', 'i', 'o', 'u']) < 3:
        return False
    if not any(word[i] == word[i + 1] for i in range(len(word) - 1)):
        return False
    return all(e not in word for e in ['ab', 'cd', 'pq', 'xy'])
print(sum(is_nice(e) for e in words))


# part 2
def is_nice2(word):
    subs = defaultdict(list)
    for i in range(len(word) - 1):
        subs[word[i:i + 2]].append(i)
    if not any(len(e) >= 2 and min(e) + 2 <= max(e) for e in subs.values()):
        return False
    return any(word[i] == word[i + 2] for i in range(len(word) - 2))
print(sum(is_nice2(e) for e in words))
