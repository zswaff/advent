from itertools import count
from collections import namedtuple
from abc import ABC, abstractmethod


class BaseAssembler(ABC):
    Result = namedtuple('Result', ['result', 'finished'])

    def __init__(self, lines, registers, print_idxs=None):
        self.print_idxs = set() if print_idxs is None else print_idxs
        self.instrs = self.process_lines(lines)
        self.registers = registers

        self.step = -1
        self.instr_idx = 0
        self.jump = None

    def print_state(self):
        print(
            f'{self.step:10} | {self.instr_idx:3} '
            + str(' '.join(str(e) for e in self.instrs[self.instr_idx])).ljust(20)
            + ' | ' + ' '.join(
                f'{k}: {v:<10}'
                for k, v in sorted(self.registers.items())
            )
        )

    def process_line(self, line):
        return [
            int(e)
            if e.isdigit() or (e.startswith('-') and e[1:].isdigit())
            else e
            for e in line.split()
        ]

    def process_lines(self, lines):
        return [self.process_line(e) for e in lines]

    @abstractmethod
    def is_finished(self):
        pass

    def is_paused(self):
        return False

    @abstractmethod
    def get_result(self):
        pass

    def eval(self, val):
        return val if isinstance(val, int) else self.registers[val]

    def run(self):
        for self.step in count(self.step + 1):
            if self.instr_idx in self.print_idxs:
                self.print_state()

            if self.is_finished():
                return BaseAssembler.Result(self.get_result(), True)

            if self.is_paused():
                return BaseAssembler.Result(self.get_result(), False)

            instr = self.instrs[self.instr_idx]
            cmd, args = instr[0], instr[1:]

            fn = self.__getattribute__(f'i__{cmd}')
            fn(*args)

            if self.jump is not None:
                self.instr_idx += self.jump
                self.jump = None
                continue
            self.instr_idx += 1
