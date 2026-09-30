# m21l01-02 · The with statement closes the file for you

**Lesson:** [Paths And Files The Modern Way](https://learnsome.tech/learn/python-course/m21l01) (lesson 21.1, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can open every file with a with statement, read it whole or line by line, append to it, choose an encoding on purpose, and build paths with pathlib that work on any operating system.

In the lesson: Here is the same job written the modern way. The word with, then the call to open exactly as before, then the word as, then a name for the file object, then a colon. Everything you want to do with that file goes in the block underneath. The moment the block ends, Python closes the file for you. There is no close line to forget, because there is no close line at all. Run it. The first print asks the file object whether it is closed and the answer is True, although we never said so anywhere. The second print opens the same file again and reads it back, and both of the lines we wrote are there.

## Files

- [`starter/withFile.py`](starter/withFile.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l01/m21l01-02/starter`
2. Read `withFile.py` the way the lesson builds it:
   - Lines 1–3: the block underneath
   - Lines 4–6: Run it
3. Notes from the lesson:
   - Line 1: with, the call to open, the word as, a name, then a colon
4. Run it: `python3 withFile.py`.
5. Check it from the repository root: `./check m21l01-02`.

## Expected output

```text
True
first line
second line

```

## How to check

`./check m21l01-02` copies `starter/` into a scratch directory and runs `python3 withFile.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
