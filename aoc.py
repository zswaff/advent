import os
import sys

import aocd


__caller = os.getcwd()
__date = {
    'day': int(__caller.split('/')[-1]),
    'year': int(__caller.split('/')[-2])
}
__puzzle = aocd.models.Puzzle(**__date)
__inp_fname = f'{__caller}/inp.txt'


if __puzzle.answered_a:
    print(f'a: {__puzzle.answer_a}')
if __puzzle.answered_b:
    print(f'b: {__puzzle.answer_b}')
    sys.exit(0)


def __submit_dest(answer):
    if not __puzzle.answered_a:
        return 'a'
    if answer != __puzzle.answer_a:
        return 'b'
    return None


def submit(answer):
    answer = str(answer)
    dest = __submit_dest(answer)
    if dest is None:
        return
    print(f'Sumbitting answer {dest} "{answer}"')
    if dest == 'a':
        __puzzle.answer_a = answer
    else:
        __puzzle.answer_b = answer


def safe_submit(answer):
    answer = str(answer)
    dest = __submit_dest(answer)
    if dest is None:
        return
    input(f'Sumbit answer {dest} "{answer}"?')
    submit(answer)


if os.path.exists(__inp_fname):
    with open(f'{__caller}/inp.txt') as fin:
        data = fin.read()
else:
    data = __puzzle.input_data
    with open(f'{__caller}/inp.txt', 'w+') as fout:
        fout.write(data)
dt = data
ls = lines = dt.split('\n')
sm = submit
ss = safe_submit
