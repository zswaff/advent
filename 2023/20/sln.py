#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from common import *


# part 1
class Mod:
    def __init__(self, targets):
        self.targets = targets

    def set_sources(self, sources):
        pass

    def pulse(self, _source, is_high):
        return [(e, is_high) for e in self.targets]

    def to_state(self):
        return None


class Flip(Mod):
    def __init__(self, targets):
        super().__init__(targets)
        self.on = False

    def pulse(self, _source, is_high):
        if is_high:
            return []
        self.on = not self.on
        return [(e, self.on) for e in self.targets]

    def to_state(self):
        return self.on


class Conj(Mod):
    def __init__(self, targets):
        super().__init__(targets)
        self.memory = None

    def set_sources(self, sources):
        self.memory = {e: False for e in sources}

    def pulse(self, source, is_high):
        self.memory[source] = is_high
        send_high = not all(self.memory.values())
        return [(e, send_high) for e in self.targets]

    def to_state(self):
        return tuple(sorted(self.memory.items()))


mods = {}
for l in ls:
    name, rtargets = l.split(" -> ")
    targets = rtargets.split(", ")
    if name == "broadcaster":
        mods[name] = Mod(targets)
        continue
    if l.startswith("%"):
        name = name[1:]
        mods[name] = Flip(targets)
        continue
    name = name[1:]
    mods[name] = Conj(targets)
rev = defaultdict(set)
for name, mod in mods.items():
    for target in mod.targets:
        rev[target].add(name)
for name, mod in mods.items():
    mod.set_sources(rev[name])

outs = []
for _ in range(1000):
    q = [("broadcaster", None, False)]
    while q:
        target, source, is_high = q.pop(0)
        outs.append(is_high)
        target_mod = mods.get(target)
        if target_mod is None:
            continue
        q += [(e, target, f) for e, f in target_mod.pulse(source, is_high)]
highs = sum(outs)
sm(highs * (len(outs) - highs))


# part 2

mods = {}
for l in ls:
    name, rtargets = l.split(" -> ")
    targets = rtargets.split(", ")
    if name == "broadcaster":
        mods[name] = Mod(targets)
        continue
    if l.startswith("%"):
        name = name[1:]
        mods[name] = Flip(targets)
        continue
    name = name[1:]
    mods[name] = Conj(targets)
rev = defaultdict(set)
for name, mod in mods.items():
    for target in mod.targets:
        rev[target].add(name)
for name, mod in mods.items():
    mod.set_sources(rev[name])

cname = list(rev["rx"])[0]
conj = mods[cname]
feeders = {e: [] for e in rev[cname]}
for i in count(1):
    q = [("broadcaster", None, False)]
    while q:
        target, source, is_high = q.pop(0)
        if source in feeders:
            if is_high:
                feeders[source].append(i)
                if all(len(e) >= 2 for e in feeders.values()):
                    break
        target_mod = mods.get(target)
        if target_mod is None:
            continue
        q += [(e, target, f) for e, f in target_mod.pulse(source, is_high)]
    else:
        continue
    break

feeders = [e[:2] for e in feeders.values()]
base, mult = feeders[0]
for b, m in feeders[1:]:
    while base % m != b:
        base += mult
    mult = lcm(mult, m)
sm(base)
