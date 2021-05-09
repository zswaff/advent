import os as __os
import sys as __sys

import aocd as __aocd


__caller = __os.getcwd()
__date = {
    'day': int(__caller.split('/')[-1]),
    'year': int(__caller.split('/')[-2])
}
__puzzle = __aocd.models.Puzzle(**__date)
__inp_fname = f'{__caller}/inp.txt'


if __puzzle.answered_a and __puzzle.answered_b:
    print(f'a: {__puzzle.answer_a}\nb: {__puzzle.answer_b}')
    __sys.exit(0)


def sa(answer):
    if __puzzle.answered_a:
        print(f'a: {__puzzle.answer_a}')
        return
    if input(f'Sumbit answer a: {answer}? ').lower().startswith('n'):
        return
    print(f'a: {answer}')
    __puzzle.answer_a = answer


def sb(answer):
    if __puzzle.answered_b:
        print(f'b: {__puzzle.answer_b}')
        return
    if input(f'Sumbit answer b: {answer}? ').lower().startswith('n'):
        return
    print(f'b: {answer}')
    __puzzle.answer_b = answer


if __os.path.exists(__inp_fname):
    with open(f'{__caller}/inp.txt') as __fin:
        dt = __fin.read()
else:
    dt = __puzzle.input_data
    with open(f'{__caller}/inp.txt', 'w+') as __fout:
        __fout.write(dt)
ls = dt.split('\n')
