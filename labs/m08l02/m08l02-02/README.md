# m08l02-02 · Trying powers in the shell

**Lesson:** [Exponents, Roots And Float Formats](https://learnsome.tech/learn/python-course/m08l02) (lesson 8.2, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can raise numbers to powers, take square roots with a fractional exponent or with the math module, and round a float for display with the format function or a format string, without changing the value itself.

In the lesson: Three to the fourth gives eighty one, exactly as arithmetic promises. The second line gives forty, not one thousand, for the precedence reason we have just discussed. The third line is the grouping demonstration. If Python grouped from the left it would square eight and give sixty four. It answers five hundred and twelve instead, because it groups from the right: three to the second is nine, and two to the ninth is five hundred and twelve. The last line makes the type explicit. A power gives an int only when both operands are integers and the correct answer really is a whole number.

## Files

- [`starter/shell-trying-powers-in-the-shell.py`](starter/shell-trying-powers-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l02/m08l02-02/starter`
2. Read `shell-trying-powers-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   3**4
   5*2**3
   2**3**2
   type(3**4)
   ```
4. Run it: `python3 -i < shell-trying-powers-in-the-shell.py`.
5. Check it from the repository root: `./check m08l02-02`.

## Expected output

```text
81
40
512
<class 'int'>
```

## How to check

`./check m08l02-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-trying-powers-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
