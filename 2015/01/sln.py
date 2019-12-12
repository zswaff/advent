from collections import Counter


with open('inp.txt') as fin:
    parens = [e for e in fin.read().strip()]


# part 1
counter = Counter(parens)
print(counter['('] - counter[')'])


# part 2
c = 0
for i, ch in enumerate(parens, 1):
    if ch == '(':
        c += 1
    if ch == ')':
        c -= 1
        if c == -1:
            print(i)
            break