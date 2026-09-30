# m22l01-02 · The function we are going to test

**Lesson:** [Testing With pytest](https://learnsome.tech/learn/python-course/m22l01) (lesson 22.1, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Graded

## Goal

You can write a test file of plain assert statements, run it with pytest, read a failure report, and say which cases are worth a test of their own.

In the lesson: Here is the code under test: a function that takes a price and a percentage off, refuses a nonsense percentage, and rounds the answer to the penny. The bottom of the file runs it twice so you can see it working, which is the by hand check we have just agreed is not enough. Twenty pounds with a tenth off is eighteen pounds, and a price with nothing off is unchanged. Keep those two answers in mind, because in a moment they stop being something you read off a screen and become something the computer checks for you. Save this as pricing dot py, and delete the two print lines once the tests exist.

## Files

- [`starter/pricing.py`](starter/pricing.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m22l01/m22l01-02/starter`
2. Read `pricing.py`.
3. Notes from the lesson:
   - Line 3: a percentage outside the sensible range is refused
4. Run it: `python3 pricing.py`.
5. Check it from the repository root: `./check m22l01-02`.

## Expected output

```text
18.0
19.99
```

## How to check

`./check m22l01-02` copies `starter/` into a scratch directory and runs `python3 pricing.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
