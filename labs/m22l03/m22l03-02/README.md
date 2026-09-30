# m22l03-02 · The parts of PEP eight that matter

**Lesson:** [Formatting, Linting And Style](https://learnsome.tech/learn/python-course/m22l03) (lesson 22.3, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Graded

## Goal

You can name and lay out code the way the rest of the Python world does, let a formatter settle the arguments, read what a linter reports, and write a docstring worth reading.

In the lesson: Four rules carry most of the weight. Naming first. Functions and variables are lower case with underscores between words. Classes are capitalised words with no underscores. Constants in capitals with underscores. You will notice this course's earlier programs use a different function naming style, because the tutorial they come from predates the convention settling; from here on, use underscores. Second, indent with four spaces and never with tabs. Third, keep lines short, around seventy nine characters, because side by side windows and code reviews are narrow. Fourth, imports go at the top of the file, one module per line, standard library first. It runs, of course; the style changed nothing but the reading.

## Files

- [`starter/styleDemo.py`](starter/styleDemo.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m22l03/m22l03-02/starter`
2. Read `styleDemo.py` the way the lesson builds it:
   - Lines 1–3: constants in capitals
   - Lines 4–8: lower case with underscores
   - Lines 9–20: capitalised words with no underscores
3. Notes from the lesson:
   - Line 3: a constant: capitals and underscores, set once
   - Line 11: a class: capitalised words joined together
4. Run it: `python3 styleDemo.py`.
5. Check it from the repository root: `./check m22l03-02`.

## Expected output

```text
3.142
6.283
```

## How to check

`./check m22l03-02` copies `starter/` into a scratch directory and runs `python3 styleDemo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
