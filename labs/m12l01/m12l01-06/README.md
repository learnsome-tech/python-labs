# m12l01-06 · Say it with a newline code

**Lesson:** [Files: Writing And Reading](https://learnsome.tech/learn/python-course/m12l01) (lesson 12.1, module 12: Files And Chapter Review) · Pro  
**Check:** Graded

## Goal

You can open a file for writing or reading, write strings to it with explicit newlines, read the whole file back as one string, and say why closing a file you wrote to is essential.

In the lesson: Here is the same program with the newline code added at the end of each string. Recall that code from the chapter on string literals: a backslash followed by the letter n, one character, standing for the end of a line. The program still prints nothing, and again the effect is on the disk. Check the contents of the file it wrote and this time the two strings sit on two lines. This is the whole difference between the write method and the print function in one example. The print function quietly adds a line ending for you. A file's write method never adds anything at all.

## Files

- [`starter/revisedFile.py`](starter/revisedFile.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m12l01/m12l01-06/starter`
2. Read `revisedFile.py`.
3. Run it: `python3 revisedFile.py`.
4. Check it from the repository root: `./check m12l01-06`.

## Expected output

```text

```

## How to check

`./check m12l01-06` copies `starter/` into a scratch directory and runs `python3 revisedFile.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m12l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
