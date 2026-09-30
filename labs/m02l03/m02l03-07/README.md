# m02l03-07 · Am I inside a virtual environment?

**Lesson:** [Installing Python On Linux](https://learnsome.tech/learn/python-course/m02l03) (lesson 2.3, module 2: Install Python Properly) · Pro  
**Check:** Graded

## Goal

You can add the Python pieces your Linux distribution leaves out with apt, dnf or pacman, understand why pip refuses to install into the system Python, answer that refusal with a virtual environment, and verify the result with python3 and pip3.

In the lesson: So how do you know which of those you are in? Python will tell you. Import sys. Print the first two numbers of the version, the pair that decides which packages will install at all. Then print whether the prefix and the base prefix are equal. The prefix is the tree Python loads its library from; the base prefix belongs to the interpreter a virtual environment was built from. Outside a virtual environment they are the same tree, so the comparison is true, as it is here. Inside one they differ and it prints false. That is more reliable than looking at your shell prompt, which any theme can hide.

## Files

- [`starter/venvcheck.py`](starter/venvcheck.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-07/starter`
2. Read `venvcheck.py` the way the lesson builds it:
   - Lines 1: Import sys
   - Lines 2–3: the first two numbers
   - Lines 4: the prefix and the base prefix
3. Notes from the lesson:
   - Line 3: The pair that decides which packages will install at all
   - Line 4: Equal outside a venv, different inside one
4. Run it: `python3 venvcheck.py`.
5. Check it from the repository root: `./check m02l03-07`.

## Expected output

```text
(3, 14)
True
```

## How to check

`./check m02l03-07` copies `starter/` into a scratch directory and runs `python3 venvcheck.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
