#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from comp import Comp


# part 1
cmp = Comp(fin='inp.txt')
out = cmp.outputs
print(sum(out[i * 3 + 2] == 2 for i in range(len(out) // 3)))


# part 2
def sign(a):
    if a == 0:
        return 0
    return 1 if a > 0 else -1


with open('inp.txt') as fin:
    ops = [int(e) for e in fin.read().strip().split(',')]
ops[0] = 2


cmp = Comp(ops=ops).add_inputs([0, 0, 0])
while True:
    out = cmp.outputs
    sb = {(out[i * 3], out[i * 3 + 1]): out[i * 3 + 2] for i in range(len(out) // 3)}
    if not any(v == 2 for v in sb.values()):
        break
    paddle = [k for k, v in sb.items() if v == 3][0]
    ball = [k for k, v in sb.items() if v == 4][0]
    cmp.add_inputs([sign(ball[0] - paddle[0])])
print(sb[(-1, 0)])
