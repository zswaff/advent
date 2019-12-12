from collections import defaultdict


with open('inp.txt') as fin:
    ops = [int(e) for e in fin.read().strip().split(',')]


def run_computer(ops, inputs, verbose=False):
    code_args = {
        1: (3, {2}),
        2: (3, {2}),
        3: (1, {0}),
        4: (1, {}),
        5: (2, {}),
        6: (2, {}),
        7: (3, {2}),
        8: (3, {2}),
        9: (1, {}),
        99: (0, {})
    }

    ops = defaultdict(int, enumerate(ops))

    outputs = []
    instr_ptr = 0
    rel_base = 0

    if verbose:
        print('ops ', [ops.get(i) for i in range(0, max(ops.keys()) + 1)])

    while True:
        if verbose:
            print('out ', outputs)
            print('-' * 100)

        full_op = ops[instr_ptr]
        op = int(str(full_op)[-2:])
        arg_count, idx_args = code_args[op]
        arg_modes = [0] * arg_count
        raw_args = [ops[i] for i in range(instr_ptr + 1, instr_ptr + arg_count + 1)]
        for i, e in enumerate(list(reversed(str(full_op)[:-2]))):
            arg_modes[i] = int(e)

        if verbose:
            print('-' * 100)
            print('ops ', [ops.get(i) for i in range(0, max(ops.keys()) + 1)])
            print('op  ', op)
            print('args', list(zip(raw_args, arg_modes)))
            print('base', rel_base)

        tot_instr_size = arg_count + 1
        args = []
        for i, (raw_arg, arg_mode) in enumerate(zip(raw_args, arg_modes)):
            if i in idx_args:
                args.append({
                    0: lambda: raw_arg,
                    1: lambda: raw_arg,
                    2: lambda: raw_arg + rel_base
                }[arg_mode]())
            else:
                args.append({
                    0: lambda: ops[raw_arg],
                    1: lambda: raw_arg,
                    2: lambda: ops[raw_arg + rel_base]
                }[arg_mode]())

        if op == 1:
            a, b, idx = args
            ops[idx] = a + b
            instr_ptr += tot_instr_size
            continue
        if op == 2:
            a, b, idx = args
            ops[idx] = a * b
            instr_ptr += tot_instr_size
            continue
        if op == 3:
            idx, = args
            if len(inputs) == 0:
                return outputs, False
            ops[idx] = inputs.pop(0)
            instr_ptr += tot_instr_size
            continue
        if op == 4:
            a, = args
            outputs.append(a)
            instr_ptr += tot_instr_size
            continue
        if op == 5:
            a, b = args
            if a:
                instr_ptr = b
            else:
                instr_ptr += tot_instr_size
            continue
        if op == 6:
            a, b = args
            if not a:
                instr_ptr = b
            else:
                instr_ptr += tot_instr_size
            continue
        if op == 7:
            a, b, idx = args
            ops[idx] = int(a < b)
            instr_ptr += tot_instr_size
            continue
        if op == 8:
            a, b, idx = args
            ops[idx] = int(a == b)
            instr_ptr += tot_instr_size
            continue
        if op == 9:
            a, = args
            rel_base += a
            instr_ptr += tot_instr_size
            continue
        if op == 99:
            return outputs, True
        raise RuntimeError('Invalid opcode')


# part 1
print(run_computer(ops, [1])[0][0])


# part 2
print(run_computer(ops, [2])[0][0])
