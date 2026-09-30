# m13l02-06 · Comparing strings, lists and floats

**Lesson:** [If Else, And Conditional Expressions](https://learnsome.tech/learn/python-course/m13l02) (lesson 13.2, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can choose between two blocks of code with an if else statement, write any of the six comparisons correctly, and test membership in a sequence with in and not in.

In the lesson: Now give x a new value and carry on. The variable does not have to be on the left of a comparison. Two strings built different ways compare as equal when they hold the same characters, and case matters. Order matters in a list too. Then comes the float surprise: point one plus point two is not equal to point three, because of the inexactness of floating point arithmetic you met earlier. Last, a comparison that makes no sense. Asking whether a letter is greater than an integer raises a TypeError, and the message names the two types Python refused to order.

## Files

- [`starter/shell-comparing-strings-lists-and-floats.py`](starter/shell-comparing-strings-lists-and-floats.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l02/m13l02-06/starter`
2. Read `shell-comparing-strings-lists-and-floats.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   x = 6
   6 == x
   6 != x
   'hi' == 'h' + 'i'
   'HI' != 'hi'
   [1, 2] != [2, 1]
   .1 + .2 == .3
   'a' > 5
   ```
4. Run it: `python3 -i < shell-comparing-strings-lists-and-floats.py`.
5. Check it from the repository root: `./check m13l02-06`.

## Expected output

```text
True
False
True
True
True
False
Traceback (most recent call last):
TypeError: '>' not supported between instances of 'str' and 'int'
```

## How to check

`./check m13l02-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-comparing-strings-lists-and-floats.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
