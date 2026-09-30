# m18l01-04 · Importing runs the file, and only once

**Lesson:** [Modules And The Import System](https://learnsome.tech/learn/python-course/m18l01) (lesson 18.1, module 18: Organising Code) · Pro  
**Check:** Graded

## Goal

You can split code across files with import, explain what happens the first time a module is imported, protect a file's own test code with the main guard, and say where Python looked to find a module.

In the lesson: You already have mathfunc dot py in your examples folder, from the module on functions. It defines a function called m, and it also prints something at the top level. Import it twice and run it. The first thing on screen is forty, which mathfunc printed itself while it was being imported. Importing does not merely make functions available; it runs the file, top to bottom, once. The second import prints nothing at all, because Python keeps a dictionary of every module it has already loaded, called sys dot modules, and a repeat import is only a lookup in it. Then fifty, from calling m through the dotted name. Then the module's own name variable, which is mathfunc. Then ours, which is dunder main. Hold on to that last line.

## Files

- [`starter/importdemo.py`](starter/importdemo.py): the listing from the lesson
- [`starter/mathfunc.py`](starter/mathfunc.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m18l01/m18l01-04/starter`
2. Read `importdemo.py` the way the lesson builds it:
   - Lines 1–4: Import it twice and run it
   - Lines 5–8: Then fifty
3. Notes from the lesson:
   - Line 3: this one runs every line of mathfunc.py
   - Line 4: this one is only a lookup in sys.modules
4. Run it: `python3 importdemo.py`.
5. Check it from the repository root: `./check m18l01-04`.

## Expected output

```text
40
50
mathfunc
__main__
```

## How to check

`./check m18l01-04` copies `starter/` into a scratch directory and runs `python3 importdemo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
