from collections import defaultdict

from comp import Comp


DRS = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}


# part 1
locs = defaultdict(int)
cmp = Comp(fin='inp.txt')
cloc, cdr = (0, 0), 0
while True:
    locs[cloc], turn = cmp.add_inputs([locs[cloc]]).last_outputs
    if cmp.finished:
        break
    cdr = (cdr + turn * 2 - 1) % 4
    cloc = cloc[0] + DRS[cdr][0], cloc[1] + DRS[cdr][1]
print(len(locs))


# part 2
locs = defaultdict(int)
cmp = Comp(fin='inp.txt')
cloc, cdr = (0, 0), 0
locs[cloc] = 1
while True:
    locs[cloc], turn = cmp.add_inputs([locs[cloc]]).last_outputs
    if cmp.finished:
        break
    cdr = (cdr + turn * 2 - 1) % 4
    cloc = cloc[0] + DRS[cdr][0], cloc[1] + DRS[cdr][1]

ls = list(locs.keys())
for y in range(max(e[1] for e in ls), min(e[1] for e in ls) - 1, -1):
    for x in range(min(e[0] for e in ls), max(e[0] for e in ls) + 1):
        print('  ' if locs[(x, y)] == 0 else '1 ', end='')
    print()
