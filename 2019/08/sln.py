from collections import Counter


x, y = 25, 6


with open('inp.txt') as fin:
    digs = [int(e) for e in fin.read().strip()]
rows = [digs[i * x:(i + 1) * x] for i in range(len(digs) // x)]
img = [rows[i * y:(i + 1) * y] for i in range(len(rows) // y)]


# part 1
res = []
for i, layer in enumerate(img):
    c = Counter(f for e in layer for f in e)
    res.append((c[0], c[1] * c[2]))
print(min(res)[1])


# part 2
res = [[2] * x for _ in range(y)]
for layer in img:
    for i, row in enumerate(layer):
        for j, dig in enumerate(row):
            if res[i][j] == 2:
                res[i][j] = dig
print('\n'.join(' '.join(str(f) for f in e) for e in res).replace('0', ' '))
