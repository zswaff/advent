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


__sub_count = 0
def sm(answer):
    global __sub_count
    if __sub_count > 1:
        return
    dest = 'a' if __sub_count == 0 else 'b'
    __sub_count += 1

    if getattr(__puzzle, f'answered_{dest}'):
        submitted = getattr(__puzzle, f'answer_{dest}')
        print(f'{dest}: {submitted}')
        return
    if input(f'Sumbit answer {dest}: {answer}? ').lower().startswith('n'):
        return
    print(f'{dest}: {answer}')
    setattr(__puzzle, f'answer_{dest}', answer)


if __os.path.exists(__inp_fname):
    with open(f'{__caller}/inp.txt') as __fin:
        dt = __fin.read()
else:
    dt = __puzzle.input_data
    with open(f'{__caller}/inp.txt', 'w+') as __fout:
        __fout.write(dt)
ls = dt.split('\n')
