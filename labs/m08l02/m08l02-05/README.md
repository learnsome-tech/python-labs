# m08l02-05 · The format function

**Lesson:** [Exponents, Roots And Float Formats](https://learnsome.tech/learn/python-course/m08l02) (lesson 8.2, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can raise numbers to powers, take square roots with a fractional exponent or with the math module, and round a float for display with the format function or a format string, without changing the value itself.

In the lesson: Read this sequence rather than racing through it. First a horrible long value goes into x. Then we call the format function with two parameters, the number and the formatting string dot five f, saving the result in s. Asking for s shows a string, quotation marks and all, holding the number rounded to five places after the decimal point. The next line asks for two places. Notice the answer: twenty three point four six, not twenty three point four five. Results are rounded, not truncated. The last line is the point of the segment. Look at x. It has not moved. It still holds every original digit. Formatting produced a new string; it did not edit the number.

## Files

- [`starter/shell-the-format-function.py`](starter/shell-the-format-function.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l02/m08l02-05/starter`
2. Read `shell-the-format-function.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   x = 23.457413902458498
   s = format(x, '.5f')
   s
   format(x, '.2f')
   x
   ```
4. Run it: `python3 -i < shell-the-format-function.py`.
5. Check it from the repository root: `./check m08l02-05`.

## Expected output

```text
'23.45741'
'23.46'
23.457413902458498
```

## How to check

`./check m08l02-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-format-function.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
