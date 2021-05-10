#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import permutations


with open('inp.txt') as fin:
    ops = [int(e) for e in fin.read().strip().split(',')]

CODE_ARG_COUNTS_AND_MODE_OVERRIDES = {
    1: (3, {2:1}),
    2: (3, {2:1}),
    3: (1, {0:1}),
    4: (1, {0:1}),
    5: (2, {}),
    6: (2, {}),
    7: (3, {2:1}),
    8: (3, {2:1}),
    99: (0, {})
}

def run_computer(ops, inputs):
    outputs = []
    instr_ptr = 0

    while True:
        full_op = ops[instr_ptr]
        op = int(str(full_op)[-2:])
        arg_count, mode_overrides = CODE_ARG_COUNTS_AND_MODE_OVERRIDES[op]
        raw_args = ops[instr_ptr + 1:instr_ptr + arg_count + 1]
        arg_modes = [int(e) for e in list(reversed(str(full_op)[:-2]))]
        arg_modes += [0] * (arg_count - len(arg_modes))
        for k, v in mode_overrides.items():
            arg_modes[k] = v

        tot_instr_size = arg_count + 1
        args = [
            raw_arg if arg_mode else ops[raw_arg]
            for raw_arg, arg_mode in zip(raw_args, arg_modes)
        ]

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
            idx, = args
            outputs.append(ops[idx])
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
        if op == 99:
            return outputs, True
        raise RuntimeError('Invalid opcode')


# part 1
outs = []
for perm in permutations(range(5)):
    out = 0
    for phase in perm:
        out = run_computer(list(ops), [phase, out])[0][0]
    outs.append(out)
print(max(outs))


# part 2
outs = []
for perm in permutations(range(5, 10)):
    i = 0
    s_inps = [[e] for e in perm]
    s_inps[0].append(0)
    o_inps = [[] for _ in range(5)]
    while True:
        inp = s_inps[i] + o_inps[i]
        out, fin = run_computer(list(ops), inp)
        if fin and i == 4:
            outs.append(out[-1])
            break
        i = (i + 1) % 5
        o_inps[i] = out
print(max(outs))
