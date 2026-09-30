# m12l01-02 · Three lines that create a file

**Lesson:** [Files: Writing And Reading](https://learnsome.tech/learn/python-course/m12l01) (lesson 12.1, module 12: Files And Chapter Review) · Pro  
**Check:** Graded

## Goal

You can open a file for writing or reading, write strings to it with explicit newlines, read the whole file back as one string, and say why closing a file you wrote to is essential.

In the lesson: Open a window on your Python program directory and note that there is no file called sample dot t x t in it. Then start Idle so that the current directory is that same folder, and run this three line program. When you run it the shell shows nothing at all: no output, no answer, no complaint. Now look back at the directory window and there is a new file. Open it in Idle, or in any word processor, and you will find the text the program wrote. This is the first program you have written whose whole effect is somewhere other than the screen.

## Files

- [`starter/firstFile.py`](starter/firstFile.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m12l01/m12l01-02/starter`
2. Read `firstFile.py`.
3. Run it: `python3 firstFile.py`.
4. Check it from the repository root: `./check m12l01-02`.

## Expected output

```text

```

## How to check

`./check m12l01-02` copies `starter/` into a scratch directory and runs `python3 firstFile.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m12l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
