# m21l01-05 · Append instead of destroying what is there

**Lesson:** [Paths And Files The Modern Way](https://learnsome.tech/learn/python-course/m21l01) (lesson 21.1, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can open every file with a with statement, read it whole or line by line, append to it, choose an encoding on purpose, and build paths with pathlib that work on any operating system.

In the lesson: Opening with the write mode empties the file first, which is the single most expensive beginner mistake with files. When you want to add to what is already there, open with the mode a, short for append. Everything you write goes on the end and nothing existing is touched. This program writes one line, appends another, and both lines survive. The last two statements show one more reading method: readlines hands back a list of strings, one per line, with the newline characters still attached. That is convenient when you want to count lines or sort them, and wasteful when the file is huge, for exactly the same reason as read.

## Files

- [`starter/appendLog.py`](starter/appendLog.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l01/m21l01-05/starter`
2. Read `appendLog.py`.
3. Run it: `python3 appendLog.py`.
4. Check it from the repository root: `./check m21l01-05`.

## Expected output

```text
started
finished
['started\n', 'finished\n']
```

## How to check

`./check m21l01-05` copies `starter/` into a scratch directory and runs `python3 appendLog.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
