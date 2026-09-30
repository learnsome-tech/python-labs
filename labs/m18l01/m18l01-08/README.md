# m18l01-08 · The trap: naming your file after a module

**Lesson:** [Modules And The Import System](https://learnsome.tech/learn/python-course/m18l01) (lesson 18.1, module 18: Organising Code) · Pro  
**Check:** Graded

## Goal

You can split code across files with import, explain what happens the first time a module is imported, protect a file's own test code with the main guard, and say where Python looked to find a module.

In the lesson: Say you are writing a dice game and you save your work as random dot py. Inside it you import random, expecting the standard library. Run that and read the three answers. The module you got is called random, its file ends in random dot py, and there is no randint in it, because the file Python found and imported was your own. The file name is the whole problem. Your folder is searched first, so your file wins, and the real module becomes unreachable from that folder. Modern Python spots this and says so in the error message, suggesting you rename the file. So do not name your files after modules you want to use: not random, not math, not email, not string.

## Files

- [`starter/random.py`](starter/random.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m18l01/m18l01-08/starter`
2. Read `random.py`.
3. Notes from the lesson:
   - Line 1: the file name is the whole problem
   - Line 8: no randint, because this is not the real module
4. Run it: `python3 random.py`.
5. Check it from the repository root: `./check m18l01-08`.

## Expected output

```text
random
True
False
```

## How to check

`./check m18l01-08` copies `starter/` into a scratch directory and runs `python3 random.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
