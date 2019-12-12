import json


with open('inp.txt') as fin:
    data = json.loads(fin.read().strip())


# part 1
def sum_recursive(d):
    if isinstance(d, int):
        return d
    if isinstance(d, str):
        return 0
    if isinstance(d, list):
        return sum(sum_recursive(e) for e in d)
    if isinstance(d, dict):
        return sum(sum_recursive(e) for e in d.values())

print(sum_recursive(data))


# part 2
def sum_recursive(d):
    if isinstance(d, int):
        return d
    if isinstance(d, str):
        return 0
    if isinstance(d, list):
        return sum(sum_recursive(e) for e in d)
    if isinstance(d, dict):
        vals = d.values()
        return 0 if 'red' in vals else sum(sum_recursive(e) for e in vals)

print(sum_recursive(data))
