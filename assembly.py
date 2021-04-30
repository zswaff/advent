from itertools import count
from abc import ABC, abstractmethod


class BaseAssembler(ABC):
    def __init__(self, lines, registers):
        self.instrs = self.process_lines(lines)
        self.registers = registers

        self.steps = -1
        self.idx = 0
        self.jump = None

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
        for self.steps in count(self.steps + 1):
            if self.is_finished():
                return True, self.get_result()

            if self.is_paused():
                return False, self.get_result()

            instr = self.instrs[self.idx]
            # print(' ' * self.registers['x'] + str(self.steps) + ' ' + str(instr))
            cmd, args = instr[0], instr[1:]

            fn = self.__getattribute__(f'i__{cmd}')
            fn(*args)

            if self.jump is not None:
                self.idx += self.jump
                self.jump = None
                continue
            self.idx += 1
