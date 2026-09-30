# m07l06-04 · Tracing functions that return values

**Lesson:** [Playing Computer](https://learnsome.tech/learn/python-course/m07l06) (lesson 7.6, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can trace a loop or a nest of function calls by hand, keeping one table row per executed line, and use that table to locate the exact line where a logical error appears.

In the lesson: Loops are not the only thing worth tracing. Here is the Python for some school mathematics: define the function m of x to be five x, let y be three, then find m of y plus m of two y minus one. The whole thing is one print statement. Just as when you simplify an expression by hand, Python must complete the innermost parts first, so each call to m has to finish and hand back a value before the addition can happen. The program prints forty. Being able to say what happened in what order is the skill we are after.

## Files

- [`starter/mathfunc.py`](starter/mathfunc.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l06/m07l06-04/starter`
2. Read `mathfunc.py`.
3. Notes from the lesson:
   - Line 5: innermost parts first: each call finishes before the addition
4. Run it: `python3 mathfunc.py`.
5. Check it from the repository root: `./check m07l06-04`.

## Expected output

```text
40
```

## How to check

`./check m07l06-04` copies `starter/` into a scratch directory and runs `python3 mathfunc.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
