# m12l01-04 · Why close is essential

**Lesson:** [Files: Writing And Reading](https://learnsome.tech/learn/python-course/m12l01) (lesson 12.1, module 12: Files And Chapter Review) · Pro  
**Check:** Graded

## Goal

You can open a file for writing or reading, write strings to it with explicit newlines, read the whole file back as one string, and say why closing a file you wrote to is essential.

In the lesson: So until the close line runs, your program still controls the file and nothing may have reached the operating system at all. That makes close essential: it makes sure everything is really written, and it hands the file back so other programs can use it. It is a common bug to write a program that adds all the data you want, and then find no file at the end. Usually that means you forgot to close it. Here is the next example, with two calls to the write method rather than one, and nothing on the screen again. Now open the file it made, because it may not hold what you expect.

## Files

- [`starter/nextFile.py`](starter/nextFile.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m12l01/m12l01-04/starter`
2. Read `nextFile.py`.
3. Run it: `python3 nextFile.py`.
4. Check it from the repository root: `./check m12l01-04`.

## Expected output

```text

```

## How to check

`./check m12l01-04` copies `starter/` into a scratch directory and runs `python3 nextFile.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m12l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
