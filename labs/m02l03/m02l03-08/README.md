# m02l03-08 · Three quick checks in the shell

**Lesson:** [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) (lesson 2.3, module 2: Install Python Properly) · Pro  
**Check:** Graded

## Goal

You can add the Python pieces your Linux distribution leaves out with apt, dnf or pacman, understand why pip refuses to install into the system Python, answer that refusal with a virtual environment, and verify the result with python3 and pip3.

In the lesson: The same questions typed straight into the shell, on a machine somebody had just handed me. Import sys, and then the two modules a Debian install can leave behind: venv, and the ensurepip module that venv needs to build anything. If either import fails, the venv package is missing, and the giveaway later is a complaint that ensurepip is not available. Ask for the minor version on its own, the number that matters when a package says which Pythons it supports; this machine says fourteen, yours may say twelve. Compare the version against a pair and you get a plain answer, which is how real code tests one. And the prefix comparison says this shell is not in a virtual environment.

## Files

- [`starter/shell-three-quick-checks-in-the-shell.py`](starter/shell-three-quick-checks-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-08/starter`
2. Read `shell-three-quick-checks-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import sys, venv, ensurepip
   sys.version_info.minor
   sys.version_info >= (3, 9)
   sys.prefix == sys.base_prefix
   ```
4. Run it: `python3 -i < shell-three-quick-checks-in-the-shell.py`.
5. Check it from the repository root: `./check m02l03-08`.

## Expected output

```text
14
True
True
```

## How to check

`./check m02l03-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-three-quick-checks-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
