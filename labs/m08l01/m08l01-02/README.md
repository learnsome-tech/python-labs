# m08l01-02 · Division always hands back a float

**Lesson:** [Floats, Division And Mixed Types](https://learnsome.tech/learn/python-course/m08l01) (lesson 8.1, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can predict whether an arithmetic expression produces an int or a float, explain why floating point results are approximations, and write code that never depends on two floats being exactly equal.

In the lesson: As you moved on in school from your first whole number division to fractions and decimals, you probably read six divided by eight as a fraction and could convert it to a decimal, point seven five. Python agrees. Now look at the second line. Six divided by three is a whole number in mathematics, yet Python answers two point zero, with a decimal point on the end. The single slash division operator always produces a float, even when the answer happens to come out even. The third line is an ordinary messy decimal. And the last line shows the real limit. Two thirds cannot be written with a finite number of digits, so Python shows around sixteen and stops. That is not a bug. That is the whole story of this module, in one line.

## Files

- [`starter/shell-division-always-hands-back-a-float.py`](starter/shell-division-always-hands-back-a-float.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l01/m08l01-02/starter`
2. Read `shell-division-always-hands-back-a-float.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   6/8
   6/3
   2.3/25.7
   2/3
   ```
4. Run it: `python3 -i < shell-division-always-hands-back-a-float.py`.
5. Check it from the repository root: `./check m08l01-02`.

## Expected output

```text
0.75
2.0
0.08949416342412451
0.6666666666666666
```

## How to check

`./check m08l01-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-division-always-hands-back-a-float.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
