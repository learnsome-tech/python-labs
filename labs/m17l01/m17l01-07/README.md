# m17l01-07 · Several except clauses, several problems

**Lesson:** [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) (lesson 17.1, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can wrap risky work in a try statement, catch the particular exception it may raise, use the as clause, else and finally correctly, and keep a program alive through bad input.

In the lesson: One try block can go wrong in more than one way, and each way may deserve a different response. This function converts its argument and divides a hundred by it, and two separate failures hide in that one line. Text that is not a number gives a ValueError from the int function. The text zero converts perfectly well and then divides badly, giving a ZeroDivisionError. So we write two except clauses, one for each, and Python picks whichever matches what was raised. Three arguments, three answers. Notice that the return inside the try block is a normal way out: when it succeeds, no handler runs at all.

## Files

- [`starter/twoproblems.py`](starter/twoproblems.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l01/m17l01-07/starter`
2. Read `twoproblems.py`.
3. Run it: `python3 twoproblems.py`.
4. Check it from the repository root: `./check m17l01-07`.

## Expected output

```text
8 -> 12.5
four -> not a number
0 -> cannot divide by zero
```

## How to check

`./check m17l01-07` copies `starter/` into a scratch directory and runs `python3 twoproblems.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
