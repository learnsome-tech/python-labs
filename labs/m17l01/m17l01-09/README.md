# m17l01-09 · finally really does mean finally

**Lesson:** [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) (lesson 17.1, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can wrap risky work in a try statement, catch the particular exception it may raise, use the as clause, else and finally correctly, and keep a program alive through bad input.

In the lesson: Here is a try statement with no except clause at all, only finally. This function is not handling anything; it is making sure something gets cleaned up. Watch both calls. The good one returns from inside the try block, and the closing line still prints before the value comes back. The bad one raises a ValueError which nothing here handles, and the closing line still prints, before the exception carries on up and ends the program. That is the guarantee: whatever route execution takes out of the try block, the finally clause runs first. Files and network connections are what this is for.

## Files

- [`starter/finallyalways.py`](starter/finallyalways.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l01/m17l01-09/starter`
2. Read `finallyalways.py`.
3. Run it: `python3 finallyalways.py`.
4. Check it from the repository root: `./check m17l01-09`.

## Expected output

```text
opening the file
closing the file
7
opening the file
closing the file
Traceback (most recent call last):
  File "finallyalways.py", line 9, in <module>
    print(load('seven'))
          ~~~~^^^^^^^^^
  File "finallyalways.py", line 4, in load
    return int(text)
ValueError: invalid literal for int() with base 10: 'seven'
```

## How to check

`./check m17l01-09` copies `starter/` into a scratch directory and runs `python3 finallyalways.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
