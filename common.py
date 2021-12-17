import re
from collections import *
from datetime import datetime, timedelta
from decimal import Decimal
from functools import *
from hashlib import md5
from itertools import *
from math import *
from operator import xor

import numpy as np
from tqdm import tqdm

from search import *
from web import *


__PATTERN_VARIABLE_FNS = {
    'i': int
}


math_e = e
del e

false = F = False
true = T = True
null = N = None


def pa(line, pattern):
    many_pats = isinstance(pattern, list)
    patterns = pattern if many_pats else [pattern]
    for idx, pat in enumerate(patterns):
        segs = [e.split('}') for e in pat.split('{')]
        assert len(segs[0]) == 1 and all(len(e) == 2 for e in segs[1:]), f'Malformed pattern {pat}'
        keys = []
        reg = '^' + re.escape(segs[0][0])
        for key, literal in segs[1:]:
            keys.append(__PATTERN_VARIABLE_FNS[key] if key else lambda x: x)
            reg += f'(.*?)' + re.escape(literal)
        reg += '$'
        mat = re.match(reg, line)
        if mat:
            if many_pats:
                return idx, (e(mat.group(i)) for i, e in enumerate(keys, 1))
            else:
                return (e(mat.group(i)) for i, e in enumerate(keys, 1))
    assert False, 'No matches'


def gr(lines, fn=None):
    if fn is None:
        fn = lambda x: x
    return {(x, y): fn(e) for y, l in enumerate(lines.split('\n')) for x, e in enumerate(l)}
