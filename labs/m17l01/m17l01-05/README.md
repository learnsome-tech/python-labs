# m17l01-05 · What a bare except costs you

**Lesson:** [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) (lesson 17.1, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can wrap risky work in a try statement, catch the particular exception it may raise, use the as clause, else and finally correctly, and keep a program alive through bad input.

In the lesson: The word except with nothing after it catches everything. That sounds robust and it is the opposite. Look at the sixth line: the length function has been misspelled, so this program raises a NameError, which has nothing to do with the failure the author had in mind. The bare handler catches it anyway, and all it says is that something went wrong. No traceback, no line number, no type name, and a real bug is now invisible. Name the exception you actually expect, so that everything you did not expect still comes out where you can see it.

## Files

- [`starter/bareexcept.py`](starter/bareexcept.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l01/m17l01-05/starter`
2. Read `bareexcept.py`.
3. Run it: `python3 bareexcept.py`.
4. Check it from the repository root: `./check m17l01-05`.

## Expected output

```text
something went wrong
```

## How to check

`./check m17l01-05` copies `starter/` into a scratch directory and runs `python3 bareexcept.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
