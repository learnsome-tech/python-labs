# m02l05-02 · Way one: the shell, for quick questions

**Lesson:** [First Run, And Fixing A Broken Install](https://learnsome.tech/learn/python-course/m02l05) (lesson 2.5, module 2: Install Python Properly) · Pro  
**Check:** Graded

## Goal

You can run Python three ways - the shell, a file from a terminal and a file from Idle - and diagnose the six failures that break a fresh install by naming the symptom, the cause and the fix.

In the lesson: Start with the shell. Type the interpreter's name at a terminal prompt, or open Idle, which opens a shell for you. Now type a sum and press Enter; the answer comes straight back. Ask it to print a greeting and it prints it. Assign a name and the shell says nothing at all, because an assignment has no value to show. Then use the name inside a call, and the greeting comes back with the name in it. Last, import the sys module and ask for the first two parts of the version. Nothing here is saved; close the window and it is gone.

## Files

- [`starter/shell-way-one-the-shell-for-quick-questions.py`](starter/shell-way-one-the-shell-for-quick-questions.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-02/starter`
2. Read `shell-way-one-the-shell-for-quick-questions.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   21 * 2
   print('Hello from the shell')
   name = 'Ada'
   print('Hello,', name)
   import sys
   sys.version_info[:2]
   ```
4. Run it: `python3 -i < shell-way-one-the-shell-for-quick-questions.py`.
5. Check it from the repository root: `./check m02l05-02`.

## Expected output

```text
42
Hello from the shell
Hello, Ada
(3, 14)
```

## How to check

`./check m02l05-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-way-one-the-shell-for-quick-questions.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
