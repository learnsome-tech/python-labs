# m21l01-03 · It closes even when the block goes wrong

**Lesson:** [Paths And Files The Modern Way](https://learnsome.tech/learn/python-course/m21l01) (lesson 21.1, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can open every file with a with statement, read it whole or line by line, append to it, choose an encoding on purpose, and build paths with pathlib that work on any operating system.

In the lesson: That promise is worth more than it sounds, so here is the proof. This program deliberately raises an error in the middle of the block, right after half a report has been written. The error is caught outside, and then we ask two questions. Was the file closed? Yes, it was. Python closes it while the error is on its way out, before anybody catches anything. And is the half written text actually on the disk? Yes, all of it. Compare that with the hand written version, where an error jumps straight over your close call and you are left with an empty file and no idea why. This is the whole argument for the with statement in one screen.

## Files

- [`starter/safeWrite.py`](starter/safeWrite.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l01/m21l01-03/starter`
2. Read `safeWrite.py`.
3. Run it: `python3 safeWrite.py`.
4. Check it from the repository root: `./check m21l01-03`.

## Expected output

```text
caught: the data ran out
file closed: True
on disk: 'half a report'
```

## How to check

`./check m21l01-03` copies `starter/` into a scratch directory and runs `python3 safeWrite.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
