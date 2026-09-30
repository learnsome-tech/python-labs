# m04l02-07 · Back to positive numbers, and the relationship

**Lesson:** [Division, Quotients And Remainders](https://learnsome.tech/learn/python-course/m04l02) (lesson 4.2, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can choose between true division, floor division and the remainder operator, predict the result of each, and explain why Python's floor division rounds down even when an operand is negative.

In the lesson: Go back to positive numbers first. Seventeen floor divide five is three, and seventeen remainder five is two. The basic relationship behind those two answers is that seventeen equals five times three plus two. Stated generally: the dividend equals the quotient times the divisor plus the remainder. We want that to always be true, whatever the signs of the numbers involved. Rearranging it gives the remainder as the dividend minus the quotient times the divisor. So once you have fixed what the integer quotient is, the remainder has no freedom left. It follows from the formula. That means the whole question about negatives is really a question about integer division.

## Files

- [`starter/shell-back-to-positive-numbers-and-the-relationshi.py`](starter/shell-back-to-positive-numbers-and-the-relationshi.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-07/starter`
2. Read `shell-back-to-positive-numbers-and-the-relationshi.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   17//5
   17%5
   ```
4. Run it: `python3 -i < shell-back-to-positive-numbers-and-the-relationshi.py`.
5. Check it from the repository root: `./check m04l02-07`.

## Expected output

```text
3
2
```

## How to check

`./check m04l02-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-back-to-positive-numbers-and-the-relationshi.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
