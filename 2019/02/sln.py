with open("inp.txt") as fin:
    ops = [int(e) for e in fin.read().strip().split(",")]

ops[1] = 12
ops[2] = 2


# part 1
def run_computer(ops):
    for i in range((len(ops) + 4) // 4):
        op = ops[i * 4]
        if op == 99:
            return ops
        a, b, idx = ops[i * 4 + 1 : (i + 1) * 4]
        if op == 1:
            ops[idx] = ops[a] + ops[b]
            continue
        if op == 2:
            ops[idx] = ops[a] * ops[b]
            continue
        raise RuntimeError("Invalid opcode")
    raise RuntimeError("Exited without finishing")


print(run_computer(list(ops))[0])


# part 2
def find_args(ops, target):
    for i in range(len(ops)):
        for j in range(len(ops)):
            t_ops = list(ops)
            t_ops[1] = i
            t_ops[2] = j
            res = run_computer(t_ops)[0]
            if res == target:
                return i, j


n, v = find_args(ops, 19690720)
print(100 * n + v)
