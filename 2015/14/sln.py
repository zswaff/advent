#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


FMT = r"(?P<name>[A-Za-z]+) can fly (?P<speed>\d+) km/s for (?P<time>\d+) seconds, but then must rest for (?P<rest>\d+) seconds."


with open("inp.txt") as fin:
    lines = [e.strip() for e in fin.readlines()]
deer = {}
for line in lines:
    match = re.match(FMT, line).groupdict()
    deer[match["name"]] = [int(match[e]) for e in ["speed", "time", "rest"]]


# part 1
def dist(speed, time, rest, interval):
    return speed * time * (interval // (time + rest)) + speed * min(time, interval % (time + rest))


print(max(dist(*e, 2503) for e in deer.values()))


# part 2
scores = {e: 0 for e in deer.keys()}
for i in range(1, 2504):
    scores[max((dist(*v, i), k) for k, v in deer.items())[1]] += 1
print(max(scores.values()))
