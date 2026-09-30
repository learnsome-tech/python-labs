# m16l01-08 · The version that is actually right

**Lesson:** [Reading Error Messages](https://learnsome.tech/learn/python-course/m16l01) (lesson 16.1, module 16: Reading Errors, And Platform Notes) · Pro  
**Check:** Graded

## Goal

You can tell a syntax error from a run time error, read a traceback from the bottom up, and follow the chain of calls above the failing line to your own code.

In the lesson: Here is the final version, with the prompt given a colon and a space and the stray bracket taken out of the last string. The final run is clean. Notice that the middle version, with the tidy prompt but the bracket still there, was a program that ran perfectly happily and printed something slightly wrong; only you could catch that. So all three kinds of error have now appeared: syntax errors found before execution, a run time error with a traceback, and logical errors that Python is content with and you must notice yourself.

## Files

- [`starter/fixMyCode.py`](starter/fixMyCode.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m16l01/m16l01-08/starter`
2. Read `fixMyCode.py`.
3. Run it: `python3 fixMyCode.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m16l01-08`.

## Expected output

```text
Enter a number: 10 more is 110
Now we are done!
```

## How to check

`./check m16l01-08` copies `starter/` into a scratch directory and runs `python3 fixMyCode.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m16l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
