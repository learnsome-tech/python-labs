# m08l02-03 · Fractional exponents give roots

**Lesson:** [Exponents, Roots And Float Formats](https://learnsome.tech/learn/python-course/m08l02) (lesson 8.2, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can raise numbers to powers, take square roots with a fractional exponent or with the math module, and round a float for display with the format function or a format string, without changing the value itself.

In the lesson: Exponents do not have to be integers, and the most useful example is the power point five, which produces a square root. Nine to the power point five is three point zero, a float even though the answer is whole, because the exponent was not an integer. Two to the power point five gives the familiar square root of two. A negative exponent gives a reciprocal: two to the minus one is point five. Python also ships a maths library, and the tutorial uses libraries like this later, so meet the pattern now. Type import math on a line of its own and the whole module becomes available under that name. The square root function inside it gives the very same answer as the fractional power.

## Files

- [`starter/shell-fractional-exponents-give-roots.py`](starter/shell-fractional-exponents-give-roots.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l02/m08l02-03/starter`
2. Read `shell-fractional-exponents-give-roots.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   9**.5
   2**.5
   2**-1
   type(9**.5)
   import math
   math.sqrt(9)
   math.sqrt(2)
   math.sqrt(2) == 2**.5
   ```
4. Run it: `python3 -i < shell-fractional-exponents-give-roots.py`.
5. Check it from the repository root: `./check m08l02-03`.

## Expected output

```text
3.0
1.4142135623730951
0.5
<class 'float'>
3.0
1.4142135623730951
True
```

## How to check

`./check m08l02-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-fractional-exponents-give-roots.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
