# m22l03-03 · A file nobody wants to read

**Lesson:** [Formatting, Linting And Style](https://learnsome.tech/learn/python-course/m22l03) (lesson 22.3, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Graded

## Goal

You can name and lay out code the way the rest of the Python world does, let a formatter settle the arguments, read what a linter reports, and write a docstring worth reading.

In the lesson: Here is the same kind of code written by somebody in a hurry. Two spaces after def, spaces inside the brackets, spaces around the default value where there should be none, no spaces around the assignment where there should be some, no blank lines anywhere, and the print jammed against the function. It works perfectly, and the answer is right, in its floating point way. But every reader now has to look twice at each line to see the structure. In a team, this is the sort of thing people argue about in code reviews, at length, and with feeling. The next segment makes the argument unnecessary.

## Files

- [`starter/messy.py`](starter/messy.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m22l03/m22l03-03/starter`
2. Read `messy.py`.
3. Run it: `python3 messy.py`.
4. Check it from the repository root: `./check m22l03-03`.

## Expected output

```text
4.050000000000001
```

## How to check

`./check m22l03-03` copies `starter/` into a scratch directory and runs `python3 messy.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
