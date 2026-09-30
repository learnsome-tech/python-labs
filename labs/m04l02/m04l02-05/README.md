# m04l02-05 · The six answers

**Lesson:** [Division, Quotients And Remainders](https://learnsome.tech/learn/python-course/m04l02) (lesson 4.2, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can choose between true division, floor division and the remainder operator, predict the result of each, and explain why Python's floor division rounds down even when an operand is negative.

In the lesson: Here are the six answers. Twenty three floor divide five is four, because five goes into twenty three four whole times. Twenty three remainder five is three, the part left over. Twenty remainder five is zero, and a zero remainder is exactly how you will test whether one number divides another exactly. Six floor divide eight is zero, since eight does not go into six even once. Six remainder eight is six: when the dividend is smaller than the divisor, the whole dividend is left over, and beginners find that one surprising. Finally six divided by eight, with the single slash, is zero point seven five. The same pair of numbers, three different questions, three different answers.

## Files

- [`starter/shell-the-six-answers.py`](starter/shell-the-six-answers.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-05/starter`
2. Read `shell-the-six-answers.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   23//5
   23%5
   20%5
   6//8
   6%8
   6/8
   ```
4. Run it: `python3 -i < shell-the-six-answers.py`.
5. Check it from the repository root: `./check m04l02-05`.

## Expected output

```text
4
3
0
0
6
0.75
```

## How to check

`./check m04l02-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-six-answers.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
