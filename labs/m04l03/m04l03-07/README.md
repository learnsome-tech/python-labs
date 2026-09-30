# m04l03-07 · Same symbol, different types

**Lesson:** [Strings, Delimiters And Concatenation](https://learnsome.tech/learn/python-course/m04l03) (lesson 4.3, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write string literals with either delimiter, tell a string of digits from an integer, concatenate and repeat strings, and fix the type error that mixing the two produces.

In the lesson: Here are the first two lines. Seven plus two as integers is nine, which is no surprise at all. Put both of them in quotes and the answer is the two character string seven two: the characters stuck end to end, not the number seventy two, and certainly not nine. Python checks the types and interprets the plus symbol based on the type. The symbol on the screen did not change between those two lines. The types did, and that changed what the symbol means. This is the first place in the course where reading the type off the screen matters more than reading the value.

## Files

- [`starter/shell-same-symbol-different-types.py`](starter/shell-same-symbol-different-types.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-07/starter`
2. Read `shell-same-symbol-different-types.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   7+2
   '7'+'2'
   ```
4. Run it: `python3 -i < shell-same-symbol-different-types.py`.
5. Check it from the repository root: `./check m04l03-07`.

## Expected output

```text
9
'72'
```

## How to check

`./check m04l03-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-same-symbol-different-types.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
