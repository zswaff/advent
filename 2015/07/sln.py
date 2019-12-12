import re


INT_MAX = 65535

UNARY_FMT = r'(?P<not>(NOT )?)(?P<num1>\d*)(?P<var1>[a-z]*) -> (?P<dest>[a-z]*)'
BINARY_FMT = r'(?P<num1>\d*)(?P<var1>[a-z]*) (?P<op>AND|OR|LSHIFT|RSHIFT) (?P<num2>\d*)(?P<var2>[a-z]*) -> (?P<dest>[a-z]*)'

with open('inp.txt') as fin:
    instrs = [e.strip() for e in fin.readlines()]


# part 1
res = {}
def eval_val(n, v):
    if n != '':
        return int(n)
    else:
        if v in res:
            return res[v]
        else:
            return None

evaled = [False] * len(instrs)
while not all(evaled):
    for i, instr in enumerate(instrs):
        u_match = re.match(UNARY_FMT, instr)
        if u_match is not None:
            nt, n1, v1, dest = [u_match[e] for e in ['not', 'num1', 'var1', 'dest']]
            p1 = eval_val(n1, v1)
            if p1 is None:
                continue
            if nt != '':
                p1 = INT_MAX ^ p1
            res[dest] = p1
            evaled[i] = True
            continue
        b_match = re.match(BINARY_FMT, instr)
        if b_match is not None:
            n1, v1, op, n2, v2, dest = [b_match[e] for e in ['num1', 'var1', 'op', 'num2', 'var2', 'dest']]
            p1 = eval_val(n1, v1)
            p2 = eval_val(n2, v2)
            if p1 is None or p2 is None:
                continue
            res[dest] = {
                'AND': p1 & p2,
                'OR': p1 | p2,
                'LSHIFT': (p1 << p2) & INT_MAX,
                'RSHIFT': p1 >> p2
            }[op]
            evaled[i] = True
            continue
        raise RuntimeError('Bad parse')
print(res['a'])


# part 2
res = {'b': res['a']}
evaled = [False] * len(instrs)
while not all(evaled):
    for i, instr in enumerate(instrs):
        u_match = re.match(UNARY_FMT, instr)
        if u_match is not None:
            nt, n1, v1, dest = [u_match[e] for e in ['not', 'num1', 'var1', 'dest']]
            if dest == 'b':
                evaled[i] = True
                continue
            p1 = eval_val(n1, v1)
            if p1 is None:
                continue
            if nt != '':
                p1 = INT_MAX ^ p1
            res[dest] = p1
            evaled[i] = True
            continue
        b_match = re.match(BINARY_FMT, instr)
        if b_match is not None:
            n1, v1, op, n2, v2, dest = [b_match[e] for e in ['num1', 'var1', 'op', 'num2', 'var2', 'dest']]
            if dest == 'b':
                evaled[i] = True
                continue
            p1 = eval_val(n1, v1)
            p2 = eval_val(n2, v2)
            if p1 is None or p2 is None:
                continue
            res[dest] = {
                'AND': p1 & p2,
                'OR': p1 | p2,
                'LSHIFT': (p1 << p2) & INT_MAX,
                'RSHIFT': p1 >> p2
            }[op]
            evaled[i] = True
            continue
        raise RuntimeError('Bad parse')
print(res['a'])
