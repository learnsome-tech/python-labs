# m16l01-04 · One error fixed, the next one named

**Lesson:** [Reading Error Messages](https://learnsome.tech/learn/python-course/m16l01) (lesson 16.1, module 16: Reading Errors, And Platform Notes) · Pro  
**Check:** Graded

## Goal

You can tell a syntax error from a run time error, read a traceback from the bottom up, and follow the chain of calls above the failing line to your own code.

In the lesson: Save the broken example under a name of your own and repair it there. The examples folder does ship a file whose name ends in FIXED, but it still holds the same planned errors, so the repairs are yours to make. First give that string literal its closing quote. Run it again. A new message, and this one is precise: a parenthesis on the line before was never closed. That is exactly the fault the tutorial predicted, hiding one line above where the first complaint appeared. When you type the missing close bracket in Idle, it briefly shows you which opening bracket it matched.

## Files

- [`starter/fixMyCode.py`](starter/fixMyCode.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

`starter/fixMyCode.py` does not parse, on purpose: the lesson shows the error it gives.

## Steps

1. Go to the starter: `cd labs/m16l01/m16l01-04/starter`
2. Read `fixMyCode.py`.
3. Run it: `python3 fixMyCode.py`.
4. Check it from the repository root: `./check m16l01-04`.

## Expected output

```text
  File "fixMyCode.py", line 3
    print('10 more is {}'.format(y)
         ^
SyntaxError: '(' was never closed
```

## How to check

`./check m16l01-04` copies `starter/` into a scratch directory and runs `python3 fixMyCode.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m16l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
