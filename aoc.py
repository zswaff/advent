import re
from collections import *
from datetime import datetime, timedelta
from decimal import Decimal
from functools import *
from hashlib import md5
from itertools import *
from math import *
from operator import xor
from typing import Any, Callable, TypeVar

import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from tqdm import tqdm
import z3

from assembly import *
from search import *
from web import *


__PATTERN_VARIABLE_INFO = {"": (".", lambda x: x), "i": (r"-?\d", int)}


math_e = e
del e

false = F = False
true = T = True
null = N = None


def __make_regex_from_pattern(pattern: str, plain=False) -> str:
    segs = [e.split("}") for e in pattern.split("{")]
    assert len(segs[0]) == 1 and all(
        len(e) == 2 for e in segs[1:]
    ), f"Malformed pattern {pattern}"
    fns = []
    res = f"{'' if plain else '^'}{re.escape(segs[0][0])}"
    for key, literal in segs[1:]:
        rc, fn = __PATTERN_VARIABLE_INFO[key]
        fns.append(fn)
        res += f"{'' if plain else '('}{rc}*?{'' if plain else ')'}{re.escape(literal)}"
    if not plain:
        res += "$"
    return res, fns


def pa(
    pattern: str | list[str], line: str
) -> tuple[Any, ...] | tuple[int, tuple[Any, ...]]:
    many_pats = isinstance(pattern, list)
    patterns = pattern if many_pats else [pattern]
    for idx, pat in enumerate(patterns):
        reg, fns = __make_regex_from_pattern(pat)
        mat = re.match(reg, line)
        if mat:
            if many_pats:
                return idx, tuple(e(mat.group(i)) for i, e in enumerate(fns, 1))
            return tuple(e(mat.group(i)) for i, e in enumerate(fns, 1))
    assert False, "No matches"


def pas(
    pattern: str | list[str], lines: list[str] | None = None
) -> list[tuple[Any, ...]] | list[tuple[int, tuple[Any, ...]]]:
    if lines is None:
        lines = ls
    return [pa(pattern, e) for e in lines]


def apa(
    pattern: str | list[str], line: str
) -> list[tuple[Any, ...]] | list[tuple[int, tuple[Any, ...]]]:
    patterns = pattern if isinstance(pattern, list) else [pattern]
    reg = "|".join(__make_regex_from_pattern(e, True)[0] for e in patterns)
    return pas(pattern, re.findall(reg, line))


_T = TypeVar("_T")


def gr(
    lines: list[str] | None = None, fn: Callable[[str], _T] | None = None
) -> dict[tuple[int, int], _T]:
    if lines is None:
        lines = ls
    if fn is None:
        fn = lambda x: x
    return {(x, y): fn(e) for y, l in enumerate(lines) for x, e in enumerate(l)}


_T = TypeVar("_T")


def cngr(
    edge_map: dict[_T, dict[_T, int]], targets: list[_T]
) -> dict[_T, dict[_T, int]]:
    class State(BaseSearchState):
        def __init__(self, loc, dist):
            super().__init__()
            self.loc = loc
            self.dist = dist

        def get_neighbors(self):
            return [State(k, self.dist + v) for k, v in edge_map[self.loc].items()]

        def process(self):
            if self.loc == target or self.loc not in targets:
                return
            tres[self.loc] = min(tres.get(self.loc, inf), self.dist)

    res = {}
    for target in targets:
        tres = {}
        State(target, 0).search()
        res[target] = tres

    return res
