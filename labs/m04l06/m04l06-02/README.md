# m04l06-02 · One argument, then several, then none

**Lesson:** [The Print Function And String Literals](https://learnsome.tech/learn/python-course/m04l06) (lesson 4.6, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can display anything you like with the print function, write a string literal that spans several lines, and read the escape codes that stand for a newline, a quote or a backslash.

In the lesson: Assign three to x and five to y, then call the print function with one argument, x. Python prints three. Now call it with six expressions separated by commas: some are literal strings, some are variables, and the last one is a sum. The print function prints as strings everything in a comma separated sequence of expressions, it separates the results with single blanks, and it advances to the next line at the end. Note that you can mix types: anything that is not already a string is automatically converted to its string representation, which is why you did not have to convert the sum yourself. You can also use it with no parameters at all, to only advance to the next line, which is how you get a blank line in your output.

## Files

- [`starter/shell-one-argument-then-several-then-none.py`](starter/shell-one-argument-then-several-then-none.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l06/m04l06-02/starter`
2. Read `shell-one-argument-then-several-then-none.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   x = 3
   y = 5
   print(x)
   print('The sum of', x, 'plus', y, 'is', x+y)
   print()
   ```
4. Run it: `python3 -i < shell-one-argument-then-several-then-none.py`.
5. Check it from the repository root: `./check m04l06-02`.

## Expected output

```text
3
The sum of 3 plus 5 is 8

```

## How to check

`./check m04l06-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-one-argument-then-several-then-none.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
