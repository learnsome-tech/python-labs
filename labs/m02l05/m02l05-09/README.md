# m02l05-09 · Symptom four: instructions written for Python two

**Lesson:** [First Run, And Fixing A Broken Install](https://learnsome.tech/learn/python-course/m02l05) (lesson 2.5, module 2: Install Python Properly) · Pro  
**Check:** Graded

## Goal

You can run Python three ways - the shell, a file from a terminal and a file from Idle - and diagnose the six failures that break a fresh install by naming the symptom, the cause and the fix.

In the lesson: Fourth symptom: a file fails on its very first line, complaining about parentheses. This happens when whatever you were copying from was written for Python version two. In version two, printing was a statement and needed no brackets. In version three it is a function call, so the old form is not valid code at all. Python spots that exact pattern and says so kindly: missing parentheses in the call to print, and did you mean print with brackets. The fix is to add the brackets, and to check the age of your source.

## Files

- [`starter/oldprint.py`](starter/oldprint.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

`starter/oldprint.py` does not parse, on purpose: the lesson shows the error it gives.

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-09/starter`
2. Read `oldprint.py`.
3. Run it: `python3 oldprint.py`.
4. Check it from the repository root: `./check m02l05-09`.

## Expected output

```text
  File "oldprint.py", line 1
    print "hello"
    ^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

## How to check

`./check m02l05-09` copies `starter/` into a scratch directory and runs `python3 oldprint.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
