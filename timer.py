import builtins
import datetime
import io


def override_print():
    t0 = datetime.datetime.now()
    print(t0.isoformat() + '\n' + '-' * 26)

    print_idx = 0
    old_print = builtins.print

    def new_print(*args, **kwargs):
        nonlocal print_idx
        tdstr = str(datetime.datetime.now() - t0).lstrip('0:.')
        fprefix = f'{print_idx:6} | {tdstr:>14} | '
        oprefix = ' ' * len(fprefix)
        print_idx += 1

        with io.StringIO() as str_out:
            kwargs['file'] = str_out
            old_print(*args, **kwargs)
            str_out.seek(0)
            msg = str_out.read()

        olines = msg.split('\n')
        nlines = [fprefix + olines[0]] + [oprefix + e for e in olines[1:-1]]
        old_print('\n'.join(nlines))

    builtins.print = new_print
