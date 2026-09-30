# m05l02-04 · An exclamation point, and a spacing problem

**Lesson:** [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) (lesson 5.2, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can read a line from the user with the input function, and convert a string of digits into a number so that arithmetic works instead of concatenation.

In the lesson: Suppose we want an exclamation point at the end. You could try this: add it as one more field in the print function. Run it and you see that it is not spaced right. There should be no space after the person's name, but the default behaviour of the print function is to separate each field with a space, so the exclamation point drifts away from the name. There are several ways to fix this, and you already know one. The hint is that the plus operation on strings adds no extra space, so you could join the name and the exclamation point into one string first.

## Files

- [`starter/hello_you.py`](starter/hello_you.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-04/starter`
2. Read `hello_you.py`.
3. Run it: `python3 hello_you.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m05l02-04`.

## Expected output

```text
Enter your name: Hello Anna !
```

## How to check

`./check m05l02-04` copies `starter/` into a scratch directory and runs `python3 hello_you.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
