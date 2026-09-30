# m02l04-08 · One file that answers which Python am I

**Lesson:** [Where Python Lives: PATH And Versions](https://learnsome.tech/learn/python-course/m02l04) (lesson 2.4, module 2: Install Python Properly) · Pro  
**Check:** Runs, not graded

## Goal

You can explain how a command name becomes a program on disk, tell python, python3 and py apart on any of the three operating systems, and ask an interpreter for its own path, version and module search path.

In the lesson: Finally, a habit worth keeping. When anything about Python surprises you, run this little file and read the answer instead of guessing. The first line prints the interpreter's own path. The second prints the version as three numbers, which is the form to test against when a program needs a minimum version. The third asks whether this is the base installation or a virtual environment, by comparing two prefixes. On the machine recording this course the answers are a Homebrew Python, version three point fourteen point seven, and true, meaning no virtual environment is active. Save that file somewhere you can find it again.

## Files

- [`starter/whichpython.py`](starter/whichpython.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-08/starter`
2. Read `whichpython.py` the way the lesson builds it:
   - Lines 1–3: the interpreter's own path
   - Lines 4: three numbers
   - Lines 5: the base installation
3. Notes from the lesson:
   - Line 4: version_info is a tuple, so it compares and sorts properly
4. Run it: `python3 whichpython.py`.
5. Check it from the repository root: `./check m02l04-08`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
/opt/homebrew/opt/python@3.14/bin/python3.14
(3, 14, 7)
True
```

## How to check

`./check m02l04-08` copies `starter/` into a scratch directory and runs `python3 whichpython.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
