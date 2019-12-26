#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from itertools import chain,combinations

from comp import Comp


CMDS = {
    'n': 'north',
    's': 'south',
    'e': 'east',
    'w': 'west',
    't': 'take',
    'd': 'drop',
    'i': 'inv'
}


# part 1
c = Comp(fname='inp.txt')

def file(idx=-1):
    with open('cmd.txt') as fin:
        c.add_ascii_inputs(fin.read().split('---')[idx])

def interact():
    print(''.join(chr(e) for e in c.outputs), end='')
    with open('cmd.txt', 'a+') as fout:
        fout.write('---\n')
        while True:
            while True:
                cm = input(', '.join(CMDS) + ' > ')
                if not cm or cm[0] in CMDS:
                    break
            if not cm:
                break
            cm = CMDS[cm[0]] + cm[1:] + '\n'
            fout.write(cm)
            print(c.add_ascii_inputs(cm).last_outputs_ascii, end='')

def search():
    os = c.add_ascii_inputs('inv\n').last_outputs_ascii[28:-11].split('\n- ')
    for cos in chain(*[combinations(os, i) for i in range(len(os) + 1)]):
        for o in os:
            c.add_ascii_inputs('drop ' + o + '\n')
        for o in cos:
            c.add_ascii_inputs('take ' + o + '\n')
        res = c.add_ascii_inputs('west\n').last_outputs_ascii
        if 'Alert!' not in res:
            print(cos)
            return

file()
print(c.last_outputs_ascii[-45:-35])


# part 2
