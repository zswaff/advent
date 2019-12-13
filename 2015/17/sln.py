from functools import lru_cache


with open('inp.txt') as fin:
    cntrs = tuple([int(e.strip()) for e in fin.readlines()])


# part 1
@lru_cache()
def rec(amt, rem):
    if amt == 0:
        return 1
    if amt < 0 or len(rem) == 0:
        return 0
    return sum(rec(amt - e, rem[i + 1:]) for i, e in enumerate(rem))

print(rec(150, cntrs))


# part 2
