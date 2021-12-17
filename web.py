import re as __re
import os as __os

import aocd as __aocd


__PATTERN_VARIABLE_FNS = {
    'i': int
}


__caller = __os.getcwd()
__date = {
    'day': int(__caller.split('/')[-1]),
    'year': int(__caller.split('/')[-2])
}
__puzzle = __aocd.models.Puzzle(**__date)
__inp_fname = f'{__caller}/inp.txt'


def pa(line, pattern):
    segs = [e.split('}') for e in pattern.split('{')]
    if not len(segs[0]) == 1 and all(len(e) == 2 for e in segs[1:]):
        print(f'Malformed pattern! {pattern}')
        return
    keys = []
    pat = '^' + __re.escape(segs[0][0])
    for key, literal in segs[1:]:
        keys.append(__PATTERN_VARIABLE_FNS[key] if key else lambda x: x)
        pat += f'(.*?)' + __re.escape(literal)
    pat += '$'
    mat = __re.match(pat, line)
    if mat is None:
        print(f'No match! {pattern} does not match {line}')
        return
    return [e(mat.group(i)) for i, e in enumerate(keys, 1)]


def gr(lines, fn=None):
    if fn is None:
        fn = lambda x: x
    return {(x, y): fn(e) for y, l in enumerate(lines.split('\n')) for x, e in enumerate(l)}


__sub_count = 0


def sm(answer):
    global __sub_count
    if __sub_count > 1:
        return
    dest = 'a' if __sub_count == 0 else 'b'
    __sub_count += 1

    answer = str(answer)
    if getattr(__puzzle, f'answered_{dest}'):
        submitted = getattr(__puzzle, f'answer_{dest}')
        if answer != submitted:
            print(f'Regression! {dest} was {submitted} and is now {answer}')
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
ss = [e.split('\n') for e in dt.split('\n\n')]
