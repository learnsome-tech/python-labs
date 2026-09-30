# m08l01-06 · Mixing integers and floats

**Lesson:** [Floats, Division And Mixed Types](https://learnsome.tech/learn/python-course/m08l01) (lesson 8.1, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can predict whether an arithmetic expression produces an int or a float, explain why floating point results are approximations, and write code that never depends on two floats being exactly equal.

In the lesson: It is often important to know the numeric type that comes back from a binary operation. Before you read each answer, guess it. The very first line is the one to stare at. Three point three minus one point one should be two point two, and Python gives you two point one nine nine and a long tail of nines and a seven. Nothing is broken. Those two literals were already approximations, and the subtraction inherited the error. The next two lines show mixing. A float with an int gives a float, whichever way round you write it. The fourth line shows that a half times six point five behaves the way mathematics says it should. And the last line is the contrast: plus with two integers stays an int.

## Files

- [`starter/shell-mixing-integers-and-floats.py`](starter/shell-mixing-integers-and-floats.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l01/m08l01-06/starter`
2. Read `shell-mixing-integers-and-floats.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   3.3 - 1.1
   2.0 + 3
   2*2.5
   (1/2)*6.5
   type(2 + 3)
   ```
4. Run it: `python3 -i < shell-mixing-integers-and-floats.py`.
5. Check it from the repository root: `./check m08l01-06`.

## Expected output

```text
2.1999999999999997
5.0
5.0
3.25
<class 'int'>
```

## How to check

`./check m08l01-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-mixing-integers-and-floats.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
