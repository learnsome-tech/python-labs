# m18l01-02 · The three ways to import

**Lesson:** [Modules And The Import System](https://learnsome.tech/learn/python-course/m18l01) (lesson 18.1, module 18: Organising Code) · Pro  
**Check:** Graded

## Goal

You can split code across files with import, explain what happens the first time a module is imported, protect a file's own test code with the main guard, and say where Python looked to find a module.

In the lesson: Start in the Shell. Plain import math gives you exactly one new name, math, and you reach inside it with a dot. Math dot sqrt of one hundred and forty four is twelve point zero, a float, as division was. The from form is different: it takes sqrt out of the module and puts it straight into your own names, so you call it with no prefix at all. The as form renames as it imports, and now m dot pi answers with pi to fifteen decimal places. The last line is the interesting one. Is math the same object as m? True. There is only ever one math module object in your program, however many names you hang on it and however many files import it.

## Files

- [`starter/shell-the-three-ways-to-import.py`](starter/shell-the-three-ways-to-import.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m18l01/m18l01-02/starter`
2. Read `shell-the-three-ways-to-import.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import math
   math.sqrt(144)
   from math import sqrt
   sqrt(144)
   import math as m
   m.pi
   math is m
   ```
4. Run it: `python3 -i < shell-the-three-ways-to-import.py`.
5. Check it from the repository root: `./check m18l01-02`.

## Expected output

```text
12.0
12.0
3.141592653589793
True
```

## How to check

`./check m18l01-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-three-ways-to-import.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
