import inspect as __inspect
import os as __os

import aocd as __aocd


__caller = __os.path.abspath(
    next(e.filename for e in __inspect.stack() if e.filename.endswith("sln.py"))
)
__spl = __caller.split("/")
__date = {"day": int(__spl[-2]), "year": int(__spl[-3])}
__puzzle = __aocd.models.Puzzle(**__date)
__inp_fname = "/".join(__spl[:-1] + ["inp.txt"])


__sub_count = 0


def sm(answer):
    global __sub_count  # pylint: disable=global-statement
    if __sub_count > 1:
        return
    dest = "a" if __sub_count == 0 else "b"
    __sub_count += 1

    answer = str(answer)
    if getattr(__puzzle, f"answered_{dest}"):
        submitted = getattr(__puzzle, f"answer_{dest}")
        if answer != submitted:
            print(f"Regression! {dest} was {submitted} and is now {answer}")
        print(f"{dest}: {submitted}")
        return

    if input(f"Sumbit answer {dest}: {answer}? ").lower().startswith("n"):
        return
    print(f"{dest}: {answer}")
    setattr(__puzzle, f"answer_{dest}", answer)


if __os.path.exists(__inp_fname):
    with open(__inp_fname, encoding="UTF-8") as __fin:
        dt = __fin.read()
else:
    dt = __puzzle.input_data
    with open(__inp_fname, "w+", encoding="UTF-8") as __fout:
        __fout.write(dt)
ls = dt.split("\n")
ss = [e.split("\n") for e in dt.split("\n\n")]
