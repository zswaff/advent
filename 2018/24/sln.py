#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *
from web import *


class Group:
    def __init__(self, good, line, bst):
        self.gd = good
        spl = line.split(" ")
        self.uc = int(spl[0])
        self.hp = int(spl[4])
        pr = spl[7:-11]
        pm = {e[0]: e for e in " ".join(pr)[1:-1].split("; ")} if pr else {}
        self.im = set(pm["i"].replace(",", "").split(" ")[2:]) if "i" in pm else set()
        self.wk = set(pm["w"].replace(",", "").split(" ")[2:]) if "w" in pm else set()
        self.dp = int(spl[-6]) + bst
        self.dt = spl[-5]
        self.iv = int(spl[-1])
        self.al = True

    @property
    def ep(self):
        return self.uc * self.dp

    def get_atk_amt(self, targ):
        if self.dt in targ.im:
            return 0
        return self.ep * (2 if self.dt in targ.wk else 1)

    def chs_targ(self, cands):
        cs = sorted([(-self.get_atk_amt(e), -e.ep, -e.iv, e) for e in cands])
        return None if not cs or cs[0][0] == 0 else cs[0][3]

    def tk_dmg(self, amt):
        self.uc -= amt // self.hp
        if self.uc <= 0:
            self.al = False


gls, bls = [e.split("\n")[1:] for e in dt.split("\n\n")]


def run(bst):
    gs = [Group(True, e, bst) for e in gls] + [Group(False, e, 0) for e in bls]
    lst = inf
    while sum(e.gd for e in gs) not in {0, len(gs)}:
        gs.sort(key=lambda x: (-x.ep, -x.iv))
        ts = []
        for g in gs:
            ts.append(g.chs_targ([f for f in gs if f.gd != g.gd and f not in ts]))
        for g, t in sorted(zip(gs, ts), key=lambda x: -x[0].iv):
            if not g.al or t is None:
                continue
            t.tk_dmg(g.get_atk_amt(t))
        gs = [e for e in gs if e.al]
        if sum(e.uc for e in gs) == lst:
            return False, None
        lst = sum(e.uc for e in gs)
    return gs[0].gd, sum(e.uc for e in gs)


# part 1
sm(run(0)[1])


# part 2
for i in count():
    w, r = run(i)
    if w:
        sm(r)
        break
