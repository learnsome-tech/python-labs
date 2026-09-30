# m22l03-05 · The same file afterwards

**Lesson:** [Formatting, Linting And Style](https://learnsome.tech/learn/python-course/m22l03) (lesson 22.3, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Graded

## Goal

You can name and lay out code the way the rest of the Python world does, let a formatter settle the arguments, read what a linter reports, and write a docstring worth reading.

In the lesson: This is what came back. Two blank lines before the definition and before the code that uses it, one space after each comma, spaces around the operators, no spaces just inside brackets, and no space around the equals sign of a default argument, which is the one rule everybody gets wrong by hand. Nothing about the meaning changed, and the answer is identical, floating point tail and all. Notice also what the formatter did not do: it left the unused import alone, because rewriting layout and removing code are different jobs with different risks. Finding that import is the next tool's business.

## Files

- [`starter/tidy.py`](starter/tidy.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m22l03/m22l03-05/starter`
2. Read `tidy.py`.
3. Notes from the lesson:
   - Line 4: no space around the default, spaces around operators
4. Run it: `python3 tidy.py`.
5. Check it from the repository root: `./check m22l03-05`.

## Expected output

```text
4.050000000000001
```

## How to check

`./check m22l03-05` copies `starter/` into a scratch directory and runs `python3 tidy.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
