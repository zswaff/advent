#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
class State(BaseSearchState):
    def __init__(self, stacks, hall, dist):
        super().__init__()
        self.stacks = stacks
        self.hall = hall
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return self.stacks == (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"))

    def get_neighbors(self):
        r = []
        for j, st in enumerate(self.stacks):
            exc = (j + 1) * 2
            if self.hall[exc]:
                continue
            lv, c = 0, st[0]
            if c is None:
                lv, c = 1, st[1]
            if c is None:
                continue
            si = ord(c) - ord("A")
            nst = (None, st[1] if lv == 0 else None)
            nsts = tuple(e if i != j else nst for i, e in enumerate(self.stacks))
            for i in range(exc + 1, 11):
                if self.hall[i] is not None:
                    break
                if i in {2, 4, 6, 8}:
                    continue
                r.append(
                    State(
                        nsts,
                        tuple(e if k != i else c for k, e in enumerate(self.hall)),
                        self.dist + (lv + 1 + i - exc) * (10**si),
                    )
                )
            for i in range(exc - 1, -1, -1):
                if self.hall[i] is not None:
                    break
                if i in {2, 4, 6, 8}:
                    continue
                r.append(
                    State(
                        nsts,
                        tuple(e if k != i else c for k, e in enumerate(self.hall)),
                        self.dist + (lv + 1 + exc - i) * (10**si),
                    )
                )
        for hi, c in enumerate(self.hall):
            if c is None:
                continue
            si = ord(c) - ord("A")
            if self.stacks[si][0] is not None:
                continue
            if self.stacks[si][1] not in {None, c}:
                continue
            exc = (si + 1) * 2
            mn, mx = min(hi, exc), max(hi, exc)
            if any(self.hall[i] is not None for i in set(range(mn, mx + 1)) - {hi}):
                continue
            lv = 0 if self.stacks[si][1] == c else 1
            nst = (c if lv == 0 else None, c)
            nsts = tuple(e if i != si else nst for i, e in enumerate(self.stacks))
            r.append(
                State(
                    nsts,
                    tuple(e if k != hi else None for k, e in enumerate(self.hall)),
                    self.dist + (mx - mn + 1 + lv) * (10**si),
                )
            )
        return r

    def get_dist_from_start(self):
        return self.dist


ssts = tuple(zip(ls[2].split("#")[3:7], ls[3].split("#")[1:5]))
sm(State(ssts, (None,) * 11, 0).search().distance)


# part 2
class State(BaseSearchState):
    def __init__(self, stacks, hall, dist):
        super().__init__({"parent"})
        self.stacks = stacks
        self.hall = hall
        self.dist = dist

    def is_valid(self):
        return True

    def is_finished(self):
        return self.stacks == (("A",) * 4, ("B",) * 4, ("C",) * 4, ("D",) * 4)

    def get_neighbors(self):
        r = []
        for j, st in enumerate(self.stacks):
            exc = (j + 1) * 2
            if self.hall[exc] or all(e is None for e in st):
                continue
            for lv, c in enumerate(st):
                if c is not None:
                    break
            si = ord(c) - ord("A")
            nst = (None,) * (lv + 1) + st[lv + 1 :]
            nsts = tuple(e if i != j else nst for i, e in enumerate(self.stacks))
            for i in range(exc + 1, 11):
                if self.hall[i] is not None:
                    break
                if i in {2, 4, 6, 8}:
                    continue
                r.append(
                    State(
                        nsts,
                        tuple(e if k != i else c for k, e in enumerate(self.hall)),
                        self.dist + (lv + 1 + i - exc) * (10**si),
                    )
                )
            for i in range(exc - 1, -1, -1):
                if self.hall[i] is not None:
                    break
                if i in {2, 4, 6, 8}:
                    continue
                r.append(
                    State(
                        nsts,
                        tuple(e if k != i else c for k, e in enumerate(self.hall)),
                        self.dist + (lv + 1 + exc - i) * (10**si),
                    )
                )
        for hi, c in enumerate(self.hall):
            if c is None:
                continue
            si = ord(c) - ord("A")
            if any(e not in {None, c} for e in self.stacks[si]):
                continue
            exc = (si + 1) * 2
            mn, mx = min(hi, exc), max(hi, exc)
            if any(self.hall[i] is not None for i in set(range(mn, mx + 1)) - {hi}):
                continue
            lv = len(self.stacks[si]) - list(reversed(self.stacks[si])).index(None) - 1
            nst = (None,) * lv + (c,) * (len(self.stacks[si]) - lv)
            nsts = tuple(e if i != si else nst for i, e in enumerate(self.stacks))
            r.append(
                State(
                    nsts,
                    tuple(e if k != hi else None for k, e in enumerate(self.hall)),
                    self.dist + (mx - mn + 1 + lv) * (10**si),
                )
            )
        return r

    def get_dist_from_start(self):
        return self.dist

    def get_dist_to_finish_heuristic(self):
        LS = {"A": 2, "B": 4, "C": 6, "D": 8}
        CS = {"A": 1, "B": 10, "C": 100, "D": 1000}
        l = len(self.stacks[0])
        r = 0
        for si in range(4):
            c = chr(ord("A") + si)
            b = False
            for i, e in enumerate(reversed(self.stacks[si])):
                if e != c:
                    b = True
                if not b:
                    continue
                r += (l - i) * CS[c]
                if e is None:
                    continue
                r += (l - i) * CS[e]
                r += min(abs(LS[c] - LS[e]), 2) * CS[e]
        for i, e in enumerate(self.hall):
            if e is None:
                continue
            r += abs(i - LS[e]) * CS[e]
        return r


ssts = tuple(
    zip(
        ls[2].split("#")[3:7],
        "   #D#C#B#A#   ".split("#")[1:5],
        "   #D#B#A#C#   ".split("#")[1:5],
        ls[3].split("#")[1:5],
    )
)
sm(State(ssts, (None,) * 11, 0).search().distance)
