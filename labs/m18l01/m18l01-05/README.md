# m18l01-05 · The main guard

**Lesson:** [Modules And The Import System](https://learnsome.tech/learn/python-course/m18l01) (lesson 18.1, module 18: Organising Code) · Pro  
**Check:** Graded

## Goal

You can split code across files with import, explain what happens the first time a module is imported, protect a file's own test code with the main guard, and say where Python looked to find a module.

In the lesson: Here is a file with two small functions, and two lines that are not functions. One prints its own name variable, and the last two are the piece of Python you will see in every project: the main guard. Every module gets a variable called name, spelled with two underscores on each side. Python sets it to dunder main in the file you actually ran, and to the module name in every file that was imported. Run it directly and the name is dunder main, so the condition is true and Ada gets greeted. That is the same habit as the main function from the tutorial, with one line added: define main, then call it only behind the guard.

## Files

- [`starter/greetings.py`](starter/greetings.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m18l01/m18l01-05/starter`
2. Read `greetings.py` the way the lesson builds it:
   - Lines 1–7: two small functions
   - Lines 8–9: prints its own name variable
   - Lines 10–12: the main guard
3. Notes from the lesson:
   - Line 9: runs on every import, wanted or not
   - Line 11: true only when this file is the program being run
4. Run it: `python3 greetings.py`.
5. Check it from the repository root: `./check m18l01-05`.

## Expected output

```text
loading greetings, name is __main__
Hello, Ada!
```

## How to check

`./check m18l01-05` copies `starter/` into a scratch directory and runs `python3 greetings.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
