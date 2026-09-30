# m08l02-07 · The same rounding inside a format string

**Lesson:** [Exponents, Roots And Float Formats](https://learnsome.tech/learn/python-course/m08l02) (lesson 8.2, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can raise numbers to powers, take square roots with a fractional exponent or with the math module, and round a float for display with the format function or a format string, without changing the value itself.

In the lesson: This rounding notation also goes inside the braces of a format string, after a colon, with no quotation marks. Three of the tutorial's shell sequences are folded together here, because they differ only in how each brace says which value to use. Set up two values first. In the third line the braces are empty before the colon, so the parameters are substituted in order, which is why x appears twice in the parameter list. In the fourth line each brace names its value, and the dictionary of all local names is handed over using the locals function with two stars in front. In the fifth, each brace gives a position number instead, so one parameter can be formatted twice, two different ways.

## Files

- [`starter/shell-the-same-rounding-inside-a-format-string.py`](starter/shell-the-same-rounding-inside-a-format-string.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l02/m08l02-07/starter`
2. Read `shell-the-same-rounding-inside-a-format-string.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   x = 2.876543
   y = 16.3591
   'x long: {:.5f}, x short: {:.3f}, y: {:.2f}.'.format(x, x, y)
   'long: {x:.5f}, short: {x:.3f}.'.format(**locals())
   'longer: {0:.5f}, shorter: {0:.3f}.'.format(x)
   ```
4. Run it: `python3 -i < shell-the-same-rounding-inside-a-format-string.py`.
5. Check it from the repository root: `./check m08l02-07`.

## Expected output

```text
'x long: 2.87654, x short: 2.877, y: 16.36.'
'long: 2.87654, short: 2.877.'
'longer: 2.87654, shorter: 2.877.'
```

## How to check

`./check m08l02-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-same-rounding-inside-a-format-string.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
