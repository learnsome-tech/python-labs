# m21l01-07 · Paths as objects, not glued together strings

**Lesson:** [Paths And Files The Modern Way](https://learnsome.tech/learn/python-course/m21l01) (lesson 21.1, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can open every file with a with statement, read it whole or line by line, append to it, choose an encoding on purpose, and build paths with pathlib that work on any operating system.

In the lesson: The pathlib module gives you a Path object instead of a string, and it is the modern way to talk about files. Make one from a name. Join it to another piece with the slash operator, which pathlib borrows for exactly this and which has nothing to do with division. Ask whether it exists, and get True or False. Then the two convenience methods you will use constantly: read text and write text, which open the file, do the one operation and close it again, all in a single call. A path also knows its own parts: the name, the suffix, the parent folder. And iterdir walks the folder and hands you a Path for everything in it. Run the whole thing and watch each answer.

## Files

- [`starter/pathParts.py`](starter/pathParts.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l01/m21l01-07/starter`
2. Read `pathParts.py` the way the lesson builds it:
   - Lines 1–7: the slash operator
   - Lines 8–12: read text and write text
   - Lines 13–16: iterdir
3. Notes from the lesson:
   - Line 5: the slash joins a path and a name; it is not division
   - Line 9: write text opens, writes and closes in one call
4. Run it: `python3 pathParts.py`.
5. Check it from the repository root: `./check m21l01-07`.

## Expected output

```text
data/note.txt
False
True
hello from pathlib
note.txt .txt data
data/note.txt
data/second.txt
```

## How to check

`./check m21l01-07` copies `starter/` into a scratch directory and runs `python3 pathParts.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
