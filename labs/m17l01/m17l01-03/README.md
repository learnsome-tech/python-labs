# m17l01-03 · The try statement

**Lesson:** [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) (lesson 17.1, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can wrap risky work in a try statement, catch the particular exception it may raise, use the as clause, else and finally correctly, and keep a program alive through bad input.

In the lesson: Here is the same program, wrapped. The word try, a colon, and then indented under it the work that might fail. After that block, the word except, then the name of the exception you are willing to handle, then a colon, and under that the handler. Run it with the word twelve again, and instead of a traceback you get a sentence. The exception was raised in the middle of the try block, so the rest of that block was abandoned and the printing line was skipped. Notice also that we name the type we expect, which makes this a promise about a single kind of failure rather than a blindfold.

## Files

- [`starter/agetry.py`](starter/agetry.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l01/m17l01-03/starter`
2. Read `agetry.py` the way the lesson builds it:
   - Lines 1–3: the work that might fail
   - Lines 4–5: the handler
3. Notes from the lesson:
   - Line 4: name the exception you expect: except ValueError, not bare except
4. Run it: `python3 agetry.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m17l01-03`.

## Expected output

```text
Your age: That was not a whole number.
```

## How to check

`./check m17l01-03` copies `starter/` into a scratch directory and runs `python3 agetry.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
