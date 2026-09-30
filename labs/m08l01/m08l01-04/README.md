# m08l01-04 · Ask Python which type you have

**Lesson:** [Floats, Division And Mixed Types](https://learnsome.tech/learn/python-course/m08l01) (lesson 8.1, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can predict whether an arithmetic expression produces an int or a float, explain why floating point results are approximations, and write code that never depends on two floats being exactly equal.

In the lesson: The type function settles any argument about which kind of number you are holding. Ask it about three point five and it reports the class float, not decimal. Ask it about minus two and it reports int. Now watch the third line. Minus two point zero is mathematically the same value as minus two, but Python calls it a float, because the literal contains a decimal point. So even a number that really is a whole number can be represented in the float type if you add a decimal point when you write it. And the last line confirms what we saw a moment ago: six divided by three may look like an integer answer, but its type is float, because the slash operator said so.

## Files

- [`starter/shell-ask-python-which-type-you-have.py`](starter/shell-ask-python-which-type-you-have.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l01/m08l01-04/starter`
2. Read `shell-ask-python-which-type-you-have.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   type(3.5)
   type(-2)
   type(-2.0)
   type(6/3)
   ```
4. Run it: `python3 -i < shell-ask-python-which-type-you-have.py`.
5. Check it from the repository root: `./check m08l01-04`.

## Expected output

```text
<class 'float'>
<class 'int'>
<class 'float'>
<class 'float'>
```

## How to check

`./check m08l01-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-ask-python-which-type-you-have.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
