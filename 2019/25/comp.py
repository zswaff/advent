from collections import defaultdict


class Comp:
    CODE_ARGS = {
        1: (3, {2}),
        2: (3, {2}),
        3: (1, {0}),
        4: (1, {}),
        5: (2, {}),
        6: (2, {}),
        7: (3, {2}),
        8: (3, {2}),
        9: (1, {}),
        99: (0, {}),
    }

    cache = {}

    def __init__(self, ops=None, fname=None, verbose=False):
        self._verbose = verbose
        if fname:
            if fname in Comp.cache:
                ops = Comp.cache[fname]
            else:
                with open(fname) as fin:
                    ops = [int(e) for e in fin.read().strip().split(",")]
                Comp.cache[fname] = ops
        self._input_ops = list(ops)

        self._ops = defaultdict(int, enumerate(self._input_ops))
        self._instr_ptr = 0
        self._rel_base = 0
        self._inputs = []
        self._input_idx = 0
        self._outputs = []
        self._paused = False
        self._last_pause_out_idx = 0
        self._finished = False
        self.run()

    def reset(self):
        self._ops = defaultdict(int, enumerate(self._input_ops))
        self._instr_ptr = 0
        self._rel_base = 0
        self._inputs = []
        self._input_idx = 0
        self._outputs = []
        self._paused = False
        self._last_pause_out_idx = 0
        self._finished = False
        self.run()

    @property
    def outputs(self):
        return list(self._outputs)

    @property
    def last_outputs(self):
        return self._outputs[self._last_pause_out_idx :]

    @property
    def last_outputs_ascii(self):
        return "".join(chr(e) for e in self._outputs[self._last_pause_out_idx :])

    @property
    def paused(self):
        return self._paused

    @property
    def finished(self):
        return self._finished

    def add_inputs(self, inputs):
        self._inputs += list(inputs)
        self.run()
        return self

    def add_ascii_inputs(self, s):
        self._inputs += list(ord(e) for e in s)
        self.run()
        return self

    def run(self):
        self._paused = False
        self._last_pause_out_idx = len(self._outputs)

        if self._verbose:
            print("ops ", [self._ops.get(i) for i in range(0, max(self._ops.keys()) + 1)])

        while True:
            if self._verbose:
                print("out ", self._outputs)
                print("-" * 100)

            full_op = self._ops[self._instr_ptr]
            op = int(str(full_op)[-2:])
            arg_count, idx_args = Comp.CODE_ARGS[op]
            arg_modes = [0] * arg_count
            raw_args = [
                self._ops[i] for i in range(self._instr_ptr + 1, self._instr_ptr + arg_count + 1)
            ]
            for i, e in enumerate(list(reversed(str(full_op)[:-2]))):
                arg_modes[i] = int(e)

            if self._verbose:
                print("-" * 100)
                print("ops ", [self._ops.get(i) for i in range(0, max(self._ops.keys()) + 1)])
                print("op  ", op)
                print("args", list(zip(raw_args, arg_modes)))
                print("base", self._rel_base)

            tot_instr_size = arg_count + 1
            args = []
            for i, (raw_arg, arg_mode) in enumerate(zip(raw_args, arg_modes)):
                if i in idx_args:
                    args.append(
                        {
                            0: lambda: raw_arg,
                            1: lambda: raw_arg,
                            2: lambda: raw_arg + self._rel_base,
                        }[arg_mode]()
                    )
                else:
                    args.append(
                        {
                            0: lambda: self._ops[raw_arg],
                            1: lambda: raw_arg,
                            2: lambda: self._ops[raw_arg + self._rel_base],
                        }[arg_mode]()
                    )

            if op == 1:
                a, b, idx = args
                self._ops[idx] = a + b
                self._instr_ptr += tot_instr_size
                continue
            if op == 2:
                a, b, idx = args
                self._ops[idx] = a * b
                self._instr_ptr += tot_instr_size
                continue
            if op == 3:
                (idx,) = args
                if self._input_idx >= len(self._inputs):
                    self._paused = True
                    return self
                self._ops[idx] = self._inputs[self._input_idx]
                self._input_idx += 1
                self._instr_ptr += tot_instr_size
                continue
            if op == 4:
                (a,) = args
                self._outputs.append(a)
                self._instr_ptr += tot_instr_size
                continue
            if op == 5:
                a, b = args
                if a:
                    self._instr_ptr = b
                else:
                    self._instr_ptr += tot_instr_size
                continue
            if op == 6:
                a, b = args
                if not a:
                    self._instr_ptr = b
                else:
                    self._instr_ptr += tot_instr_size
                continue
            if op == 7:
                a, b, idx = args
                self._ops[idx] = int(a < b)
                self._instr_ptr += tot_instr_size
                continue
            if op == 8:
                a, b, idx = args
                self._ops[idx] = int(a == b)
                self._instr_ptr += tot_instr_size
                continue
            if op == 9:
                (a,) = args
                self._rel_base += a
                self._instr_ptr += tot_instr_size
                continue
            if op == 99:
                self._finished = True
                return self
            raise RuntimeError("Invalid opcode")
