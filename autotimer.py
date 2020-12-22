import builtins
import datetime
from io import StringIO


__t0 = datetime.datetime.now()
__pidx = 0


print(__t0.isoformat() + '\n' + '-' * 26)


__old_print = builtins.print


def __new_print(*args, **kwargs):
    global __pidx
    now = datetime.datetime.now()
    tdstr = str(now - __t0).lstrip('0:.')
    fprefix = f'{__pidx:6} | {tdstr:>14} | '
    oprefix = ' ' * len(fprefix)
    __pidx += 1

    with StringIO() as str_out:
        kwargs['file'] = str_out
        __old_print(*args, **kwargs)
        str_out.seek(0)
        msg = str_out.read()

    olines = msg.split('\n')
    nlines = [fprefix + olines[0]] + [oprefix + e for e in olines[1:-1]]
    __old_print('\n'.join(nlines))


builtins.print = __new_print


def quit():
    builtins.print = __old_print
