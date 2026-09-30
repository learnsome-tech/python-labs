# m02l05-10 · Symptom five: no tkinter, so Idle will not start

**Lesson:** [First Run, And Fixing A Broken Install](https://learnsome.tech/learn/python-course/m02l05) (lesson 2.5, module 2: Install Python Properly) · Pro  
**Check:** Runs, not graded

## Goal

You can run Python three ways - the shell, a file from a terminal and a file from Idle - and diagnose the six failures that break a fresh install by naming the symptom, the cause and the fix.

In the lesson: Fifth symptom: Idle refuses to start, or the graphics module fails on its first import. Behind Idle is a graphical toolkit called tk, reached from Python through a module called tkinter. It is not part of the interpreter; it is a separate piece installed alongside it. Ask for it directly and you find out at once. On the machine recording this course it is genuinely missing, and notice that the error names the private module underneath, the one with the leading underscore, rather than the friendly name you asked for. That is the text to search for.

## Files

- [`starter/tkcheck.py`](starter/tkcheck.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-10/starter`
2. Read `tkcheck.py`.
3. Run it: `python3 tkcheck.py`.
4. Check it from the repository root: `./check m02l05-10`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
Traceback (most recent call last):
  File "tkcheck.py", line 1, in <module>
    import tkinter
ModuleNotFoundError: No module named '_tkinter'
```

## How to check

`./check m02l05-10` copies `starter/` into a scratch directory and runs `python3 tkcheck.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
