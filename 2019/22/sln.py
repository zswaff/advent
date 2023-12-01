#!/usr/bin/env python3
# -*- coding: utf-8 -*-20


with open("inp.txt") as fin:
    lines = [e.strip().rsplit(" ", 1) for e in fin.readlines()]


# part 1
t = 10007
l = list(range(t))
for op, e in lines:
    if op == "deal into new":
        l = list(reversed(l))
        continue
    if op == "cut":
        l = l[int(e) :] + l[: int(e)]
        continue
    if op == "deal with increment":
        nd = {}
        for i in range(t):
            nd[(i * int(e)) % t] = l[i]
        l = [nd[i] for i in range(t)]
        continue
print(l.index(2019))


# part 2
t = 119315717514047
n = 101741582076661


def mod_inv(num, modulus):
    num %= modulus

    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y

    g, x, y = egcd(num, modulus)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % modulus


def shuff_inv(idx):
    r = idx
    for op, e in reversed(lines):
        if op == "deal into new":
            r = t - r - 1
            continue
        if op == "cut":
            r = (r + int(e)) % t
            continue
        if op == "deal with increment":
            r = (mod_inv(int(e), t)) * r % t
            continue
    return r


# y = ax + b
x1 = 1
y1 = shuff_inv(x1)
x2 = 2
y2 = shuff_inv(x2)

# y1 - y2 = a(x1 - x2)
a = (y1 - y2) * mod_inv(x1 - x2, t) % t
b = (y1 - a) % t

# yf = a(a(...) + b) + b
#    = a ** n * xi + b * (a ** (n-1) + ... + 1)
#    = a ** n * xi + b * (a ** n - 1) / (a - 1)
print(2020 * pow(a, n, t) % t + b * (pow(a, n, t) - 1) * mod_inv(a - 1, t) % t)
