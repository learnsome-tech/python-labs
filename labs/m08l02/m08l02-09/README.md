# m08l02-09 · Twenty digits of the truth

**Lesson:** [Exponents, Roots And Float Formats](https://learnsome.tech/learn/python-course/m08l02) (lesson 8.2, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can raise numbers to powers, take square roots with a fractional exponent or with the math module, and round a float for display with the format function or a format string, without changing the value itself.

In the lesson: Now use formatting for the opposite purpose. Instead of hiding digits, ask for far more of them than usual, and you can check that Python does not remember even simple decimal numbers exactly. Point one to twenty places is not point one followed by zeros. Point two is not either. The sum of the two, again to twenty places, comes out just above three tenths, while the last line shows the stored value of point three sitting just below it. Python keeps numbers correctly to about sixteen or seventeen digits. You may not care about errors that small, but this is the evidence behind the equality test from the previous module.

## Files

- [`starter/shell-twenty-digits-of-the-truth.py`](starter/shell-twenty-digits-of-the-truth.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l02/m08l02-09/starter`
2. Read `shell-twenty-digits-of-the-truth.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   format(.1, '.20f')
   format(.2, '.20f')
   format(.1 + .2, '.20f')
   format(.3, '.20f')
   ```
4. Run it: `python3 -i < shell-twenty-digits-of-the-truth.py`.
5. Check it from the repository root: `./check m08l02-09`.

## Expected output

```text
'0.10000000000000000555'
'0.20000000000000001110'
'0.30000000000000004441'
'0.29999999999999998890'
```

## How to check

`./check m08l02-09` copies `starter/` into a scratch directory and runs `python3 -i < shell-twenty-digits-of-the-truth.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
