# m02l02-11 · The same checks, typed into the shell

**Lesson:** [Installing Python On A Mac](https://learnsome.tech/learn/python-course/m02l02) (lesson 2.2, module 2: Install Python Properly) · Pro  
**Check:** Runs, not graded

## Goal

You can install your own Python on a Mac by either the python.org installer or Homebrew, leave Apple's system python3 untouched, put yours first on PATH from your zsh profile, and confirm the result with python3 and idle3.

In the lesson: Now the same questions one line at a time, which is what I would do on a machine I had never seen. Import both modules. Ask for the version information and you get a named tuple, with the release level spelled out at the end. Ask for the platform, and a Mac says darwin, the name of the system underneath macOS. Ask the platform module for the machine, and Apple silicon says arm sixty-four. The prefix confirms which installation this shell belongs to. The last line is the Tk test: here the import fails, and the message names the small extension module that talks to Tk.

## Files

- [`starter/shell-the-same-checks-typed-into-the-shell.py`](starter/shell-the-same-checks-typed-into-the-shell.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-11/starter`
2. Read `shell-the-same-checks-typed-into-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import sys, platform
   sys.version_info
   sys.platform
   platform.machine()
   sys.prefix
   import tkinter
   ```
4. Run it: `python3 -i < shell-the-same-checks-typed-into-the-shell.py`.
5. Check it from the repository root: `./check m02l02-11`.

## How to check

`./check m02l02-11` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-same-checks-typed-into-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
