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
from tqdm import tqdm

from assembly import *
from search import *
from web import *


__PATTERN_VARIABLE_FNS = {"i": int}


math_e = e
del e

false = F = False
true = T = True
null = N = None


def pa(
    line: str, pattern: str | list[str]
) -> tuple[Any, ...] | tuple[int, tuple[Any, ...]]:
    many_pats = isinstance(pattern, list)
    patterns = pattern if many_pats else [pattern]
    for idx, pat in enumerate(patterns):
        segs = [e.split("}") for e in pat.split("{")]
        assert len(segs[0]) == 1 and all(
            len(e) == 2 for e in segs[1:]
        ), f"Malformed pattern {pat}"
        keys = []
        reg = f"^{re.escape(segs[0][0])}"
        for key, literal in segs[1:]:
            keys.append(__PATTERN_VARIABLE_FNS[key] if key else lambda x: x)
            reg += f"(.*?){re.escape(literal)}"
        reg += "$"
        mat = re.match(reg, line)
        if mat:
            if many_pats:
                return idx, tuple(e(mat.group(i)) for i, e in enumerate(keys, 1))
            return tuple(e(mat.group(i)) for i, e in enumerate(keys, 1))
    assert False, "No matches"


_T = TypeVar("_T")


def gr(
    lines: list[str], fn: Callable[[str], _T] | None = None
) -> dict[tuple[int, int], _T]:
    if fn is None:
        fn = lambda x: x  # pylint: disable=unnecessary-lambda-assignment
    return {(x, y): fn(e) for y, l in enumerate(lines) for x, e in enumerate(l)}


_T = TypeVar("_T")


def cngr(
    edge_map: dict[_T, dict[_T, int]], targets: list[_T]
) -> dict[_T, dict[_T, int]]:
    class State(BaseSearchState):
        def __init__(self, loc, dist):  # pylint: disable=redefined-outer-name
            super().__init__()
            self.loc = loc
            self.dist = dist

        def is_valid(self):
            return True

        def is_finished(self):
            return False

        def get_neighbors(self):
            return [State(k, self.dist + v) for k, v in edge_map[self.loc].items()]

        def get_dist_from_start(self):
            return self.dist

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
