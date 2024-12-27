#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aoc import *


# part 1
A = "A"
RK = {(1, 0): (0, -1), (2, 0): A, (0, 1): (-1, 0), (1, 1): (0, 1), (2, 1): (1, 0)}
FK = {
    (0, 0): 7,
    (1, 0): 8,
    (2, 0): 9,
    (0, 1): 4,
    (1, 1): 5,
    (2, 1): 6,
    (0, 2): 1,
    (1, 2): 2,
    (2, 2): 3,
    (1, 3): 0,
    (2, 3): A,
}


class State(BaseSearchState):
    def __init__(self, tgt, msg, r1, r2, f, dist):
        super().__init__()
        self.tgt = tgt
        self.msg = msg
        self.r1 = r1
        self.r2 = r2
        self.f = f
        self.dist = dist

    def is_valid(self):
        return (
            self.tgt.startswith(self.msg)
            and self.r1 in RK
            and self.r2 in RK
            and self.f in FK
        )

    def is_finished(self):
        return self.msg == self.tgt

    def get_neighbors(self):
        res = [
            State(
                self.tgt,
                self.msg,
                (self.r1[0] + d[0], self.r1[1] + d[1]),
                self.r2,
                self.f,
                self.dist + 1,
            )
            for d in RK.values()
            if d != A
        ]
        d = RK[self.r1]
        if d != A:
            res.append(
                State(
                    self.tgt,
                    self.msg,
                    self.r1,
                    (self.r2[0] + d[0], self.r2[1] + d[1]),
                    self.f,
                    self.dist + 1,
                )
            )
            return res
        d = RK[self.r2]
        if d != A:
            res.append(
                State(
                    self.tgt,
                    self.msg,
                    self.r1,
                    self.r2,
                    (self.f[0] + d[0], self.f[1] + d[1]),
                    self.dist + 1,
                )
            )
            return res
        res.append(
            State(
                self.tgt,
                self.msg + str(FK[self.f]),
                self.r1,
                self.r2,
                self.f,
                self.dist + 1,
            )
        )
        return res


sm(
    sum(
        int(l[:-1]) * State(l, "", (2, 0), (2, 0), (2, 3), 0).search().distance
        for l in ls
    )
)


# part 2
L1PS = [
    "<^^^AvvvA^^Avv>A",
    "^<<A^^A>vvvA>A",
    "^<<A>A^^>AvvvA",
    "<^A^^Avv>AvA",
    "<^^A<A>vvA>A",
]
RM = {
    ("AA"): "A",
    ("A^"): "<A",
    ("A<"): "v<<A",
    ("Av"): "<vA",
    ("A>"): "vA",
    ("^A"): ">A",
    ("^^"): "A",
    ("^<"): "v<A",
    ("^>"): "v>A",
    ("<A"): ">>^A",
    ("<^"): ">^A",
    ("<<"): "A",
    ("<v"): ">A",
    ("vA"): "^>A",
    ("v<"): "<A",
    ("vv"): "A",
    ("v>"): ">A",
    (">A"): "^A",
    (">^"): "<^A",
    (">v"): "<A",
    (">>"): "A",
}

rrm = {}
for k, v in RM.items():
    rrm[k] = Counter()
    rrm[k][f"A{v[0]}"] += 1
    for a, b in zip(v, v[1:]):
        rrm[k][f"{a}{b}"] += 1
foo = set()
c = 0
for l, l1p in zip(ls, L1PS):
    lm = Counter()
    lm[f"A{l1p[0]}"] += 1
    for a, b in zip(l1p, l1p[1:]):
        lm[f"{a}{b}"] += 1
    for _ in range(25):
        nlm = Counter()
        for k, v in lm.items():
            foo.add(k)
            for k2, v2 in rrm[k].items():
                nlm[k2] += v * v2
        lm = nlm
    c += int(l[:-1]) * sum(lm.values())
sm(c)
