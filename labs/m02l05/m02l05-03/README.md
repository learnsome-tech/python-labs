# m02l05-03 · Way two: your first file, from a terminal

**Lesson:** [First Run, And Fixing A Broken Install](https://learnsome.tech/learn/python-course/m02l05) (lesson 2.5, module 2: Install Python Properly) · Pro  
**Check:** Graded

## Goal

You can run Python three ways - the shell, a file from a terminal and a file from Idle - and diagnose the six failures that break a fresh install by naming the symptom, the cause and the fix.

In the lesson: Now the same idea, but saved. Open a new file, type these lines, and save it into your Python folder under a name ending in dot py. That ending matters to your editor, which uses it to colour the code, and on Windows it is what associates the file with Python. Save it, open a terminal in the folder you saved it in, and name the interpreter and then the file. It prints both lines and hands your prompt back. That is a program: text in a file, given to the interpreter, run from the top down, and finished.

## Files

- [`starter/hello.py`](starter/hello.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-03/starter`
2. Read `hello.py` the way the lesson builds it:
   - Lines 1: type these lines
   - Lines 2–4: Save it
3. Notes from the lesson:
   - Line 1: A docstring: a note for humans, ignored by the interpreter
4. Run it: `python3 hello.py`.
5. Check it from the repository root: `./check m02l05-03`.

## Expected output

```text
Hello from my own Python.
It works.
```

## How to check

`./check m02l05-03` copies `starter/` into a scratch directory and runs `python3 hello.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
