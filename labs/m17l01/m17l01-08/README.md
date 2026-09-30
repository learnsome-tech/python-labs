# m17l01-08 · Exactly when else and finally run

**Lesson:** [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) (lesson 17.1, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can wrap risky work in a try statement, catch the particular exception it may raise, use the as clause, else and finally correctly, and keep a program alive through bad input.

In the lesson: The quickest way to learn else and finally is to make each clause announce itself. Compare the two runs on screen. With a good argument the try block finishes, so the else clause runs and the except clause does not. With a bad one the except clause runs and the else clause does not. In both cases the finally clause runs, and it runs last. Why have an else clause, when you could put that line at the end of the try block? Because anything inside the try block is also protected, and you do not want to catch a ValueError raised by your follow up work.

## Files

- [`starter/elsefinally.py`](starter/elsefinally.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l01/m17l01-08/starter`
2. Read `elsefinally.py`.
3. Run it: `python3 elsefinally.py`.
4. Check it from the repository root: `./check m17l01-08`.

## Expected output

```text
trying 7
- else ran, value is 7
- finally ran
trying seven
- except ran
- finally ran
```

## How to check

`./check m17l01-08` copies `starter/` into a scratch directory and runs `python3 elsefinally.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
