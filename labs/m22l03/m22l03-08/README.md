# m22l03-08 · Docstrings: the note the code cannot give

**Lesson:** [Formatting, Linting And Style](https://learnsome.tech/learn/python-course/m22l03) (lesson 22.3, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Graded

## Goal

You can name and lay out code the way the rest of the Python world does, let a formatter settle the arguments, read what a linter reports, and write a docstring worth reading.

In the lesson: The last piece of style is the docstring: a string as the very first thing inside a function, class or file. You met them early in this course as a note at the top of a program. The convention is a single summary line, written as a command rather than a description, then a blank line, then any detail worth having. Python keeps it, which is the difference between a docstring and a comment: it lands in the doc attribute, the help function prints it, and your editor shows it when you call the function. The third line of output reads the summary straight out of the running program.

## Files

- [`starter/postage.py`](starter/postage.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m22l03/m22l03-08/starter`
2. Read `postage.py`.
3. Notes from the lesson:
   - Line 2: one summary line, in the imperative: Return, not Returns
4. Run it: `python3 postage.py`.
5. Check it from the repository root: `./check m22l03-08`.

## Expected output

```text
5.5
11.0
Return the postage in pounds for a parcel.
```

## How to check

`./check m22l03-08` copies `starter/` into a scratch directory and runs `python3 postage.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
