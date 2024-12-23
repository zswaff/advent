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
class State(BaseSearchState):
    def __init__(self, tgt, msg, rs, f, dist):
        super().__init__()
        self.tgt = tgt
        self.msg = msg
        self.rs = rs
        self.f = f
        self.dist = dist

    def is_valid(self):
        return (
            self.tgt.startswith(self.msg)
            and all(e in RK for e in self.rs)
            and self.f in FK
        )

    def is_finished(self):
        return self.msg == self.tgt

    def get_neighbors(self):
        r = self.rs[0]
        res = [
            State(
                self.tgt,
                self.msg,
                (r[0] + d[0], r[1] + d[1]) + self.rs[1:],
                self.f,
                self.dist + 1,
            )
            for d in RK.values()
            if d != A
        ]
        for i, e in enumerate(self.rs[:-1]):
            d = RK[e]
            if d != A:
                r = self.rs[i + 1]
                res.append(
                    State(
                        self.tgt,
                        self.msg,
                        self.rs[: i + 1]
                        + (r[0] + d[0], r[1] + d[1])
                        + self.rs[i + 2 :],
                        self.f,
                        self.dist + 1,
                    )
                )
                return res
        d = RK[self.rs[-1]]
        if d != A:
            res.append(
                State(
                    self.tgt,
                    self.msg,
                    self.rs,
                    (self.f[0] + d[0], self.f[1] + d[1]),
                    self.dist + 1,
                )
            )
            return res
        res.append(
            State(
                self.tgt,
                self.msg + str(FK[self.f]),
                self.rs,
                self.f,
                self.dist + 1,
            )
        )
        return res


sm(
    sum(
        int(l[:-1]) * State(l, "", ((2, 0),) * 25, (2, 3), 0).search().distance
        for l in ls
    )
)
