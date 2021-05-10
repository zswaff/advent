#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('inp.txt') as fin:
    instrs = [e.strip() for e in fin.readlines()]


# part 1
s = 'abcdefgh'
for instr in instrs:
    splt = instr.split(' ')
    if instr.startswith('swap position'):
        c1, c2 = s[int(splt[2])], s[int(splt[5])]
        s = s.replace(c1, '.').replace(c2, c1).replace('.', c2)
        continue
    if instr.startswith('swap letter'):
        c1, c2 = splt[2], splt[5]
        s = s.replace(c1, '.').replace(c2, c1).replace('.', c2)
        continue
    if instr.startswith('rotate left'):
        p = int(splt[2])
        s = s[p:] + s[:p]
        continue
    if instr.startswith('rotate right'):
        p = int(splt[2])
        s = s[-p:] + s[:-p]
        continue
    if instr.startswith('rotate based'):
        c = splt[6]
        p = s.index(c)
        r = (1 + p + (0 if p < 4 else 1)) % len(s)
        s = s[-r:] + s[:-r]
        continue
    if instr.startswith('reverse'):
        p1, p2 = int(splt[2]), int(splt[4])
        s = s[:p1] + ''.join(reversed(s[p1:p2+1])) + s[p2+1:]
        continue
    if instr.startswith('move'):
        p1, p2 = int(splt[2]), int(splt[5])
        l = list(s)
        l.insert(p2, l.pop(p1))
        s = ''.join(l)
        continue
print(s)


# part 2
s = 'fbgdceah'
for instr in reversed(instrs):
    splt = instr.split(' ')
    if instr.startswith('swap position'):
        c1, c2 = s[int(splt[2])], s[int(splt[5])]
        s = s.replace(c1, '.').replace(c2, c1).replace('.', c2)
        continue
    if instr.startswith('swap letter'):
        c1, c2 = splt[2], splt[5]
        s = s.replace(c1, '.').replace(c2, c1).replace('.', c2)
        continue
    if instr.startswith('rotate left'):
        p = int(splt[2])
        s = s[-p:] + s[:-p]
        continue
    if instr.startswith('rotate right'):
        p = int(splt[2])
        s = s[p:] + s[:p]
        continue
    if instr.startswith('rotate based'):
        c = splt[6]
        for i in range(len(s)):
            p = s.index(c)
            if i == (1 + p + (0 if p < 4 else 1)) % len(s):
                break
            s = s[1:] + s[:1]
        continue
    if instr.startswith('reverse'):
        p1, p2 = int(splt[2]), int(splt[4])
        s = s[:p1] + ''.join(reversed(s[p1:p2+1])) + s[p2+1:]
        continue
    if instr.startswith('move'):
        p2, p1 = int(splt[2]), int(splt[5])
        l = list(s)
        l.insert(p2, l.pop(p1))
        s = ''.join(l)
        continue
print(s)
