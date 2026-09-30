# m17l01-11 · Surviving bad input for as long as it takes

**Lesson:** [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) (lesson 17.1, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can wrap risky work in a try statement, catch the particular exception it may raise, use the as clause, else and finally correctly, and keep a program alive through bad input.

In the lesson: Now put the pieces together into the thing you will write again and again: a function that refuses to hand back anything but a whole number. An endless loop, an input call, and a try block. The return is inside the try block, so a successful conversion leaves the function and the loop at once. If the conversion raises a ValueError we print a complaint and fall off the bottom of the handler, and the loop goes round again. Three answers went in here: the word twelve, then an empty line, which the int function likes no better, and then a real number. Only when the caller gets a number does the last line run.

## Files

- [`starter/asknumber.py`](starter/asknumber.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l01/m17l01-11/starter`
2. Read `asknumber.py` the way the lesson builds it:
   - Lines 1–3: an endless loop
   - Lines 4–5: the return is inside the try block
   - Lines 6–7: the loop goes round again
   - Lines 8–10: the caller gets a number
3. Run it: `python3 asknumber.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m17l01-11`.

## Expected output

```text
Your age: Please type a whole number.
Your age: Please type a whole number.
Your age: Next year you will be 13
```

## How to check

`./check m17l01-11` copies `starter/` into a scratch directory and runs `python3 asknumber.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
