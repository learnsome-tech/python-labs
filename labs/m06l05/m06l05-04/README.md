# m06l05-04 · Returning a string, with local variables

**Lesson:** [Returning Values](https://learnsome.tech/learn/python-course/m06l05) (lesson 6.5, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function that returns a value, use a call inside a larger expression, and tell the difference between a function that prints and a function that returns.

In the lesson: Python functions can return any type of data, not just numbers, and there can be any number of statements before the return statement. Follow and run example program return two. The function lastFirst has two formal parameters, a first name and a last name. Its body has a new feature: the variables separator and result are given values inside the function, and neither of them is among the formal parameters. The assignments work as you would expect. Line four sets separator to a comma and a space. Line five builds the result by joining the last name, the separator and the first name. Line six returns it, and the caller prints what came back. More on those inside variables shortly.

## Files

- [`starter/return2.py`](starter/return2.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-04/starter`
2. Read `return2.py` the way the lesson builds it:
   - Lines 1–6: two formal parameters
   - Lines 7–9: the caller prints
3. Notes from the lesson:
   - Line 4: separator is not a parameter; it is created here
   - Line 6: any type of data may be returned
4. Run it: `python3 return2.py`.
5. Check it from the repository root: `./check m06l05-04`.

## Expected output

```text
Franklin, Benjamin
Harrington, Andrew
```

## How to check

`./check m06l05-04` copies `starter/` into a scratch directory and runs `python3 return2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
