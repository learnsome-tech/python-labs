# m04l02-03 · The quotient and the remainder, separately

**Lesson:** [Division, Quotients And Remainders](https://learnsome.tech/learn/python-course/m04l02) (lesson 4.2, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can choose between true division, floor division and the remainder operator, predict the result of each, and explain why Python's floor division rounds down even when an operand is negative.

In the lesson: In early grade school you would likely say fourteen divided by four is three with a remainder of two. The problem here is that the answer is in two parts, the integer quotient three and the remainder two, and neither of these results is the same as the decimal result. Python has separate operations to generate each part. Type fourteen divided by four again for the decimal answer. Then use the doubled division symbol, for the operation that produces just the integer quotient, and you get three. Then use the percent sign, which Python introduces for the operation of finding the remainder, and you get two. Finding remainders will prove more useful than you might think in the future.

## Files

- [`starter/shell-the-quotient-and-the-remainder-separately.py`](starter/shell-the-quotient-and-the-remainder-separately.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-03/starter`
2. Read `shell-the-quotient-and-the-remainder-separately.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   14/4
   14//4
   14%4
   ```
4. Run it: `python3 -i < shell-the-quotient-and-the-remainder-separately.py`.
5. Check it from the repository root: `./check m04l02-03`.

## Expected output

```text
3.5
3
2
```

## How to check

`./check m04l02-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-quotient-and-the-remainder-separately.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
