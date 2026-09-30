# m13l02-05 · Testing equality changes nothing

**Lesson:** [If Else, And Conditional Expressions](https://learnsome.tech/learn/python-course/m13l02) (lesson 13.2, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can choose between two blocks of code with an if else statement, write any of the six comparisons correctly, and test membership in a sequence with in and not in.

In the lesson: Predict each answer before you press return. Assign five to x, then ask for x, and the shell shows you five. Test it against five with the double equals and you get True. Test it against six and you get False. Now look at what has not happened: neither test changed x. A test for equality does not make an assignment, and it does not need a variable on the left hand side either. Finally, x not equal to six is True.

## Files

- [`starter/shell-testing-equality-changes-nothing.py`](starter/shell-testing-equality-changes-nothing.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l02/m13l02-05/starter`
2. Read `shell-testing-equality-changes-nothing.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   x = 5
   x
   x == 5
   x == 6
   x != 6
   ```
4. Run it: `python3 -i < shell-testing-equality-changes-nothing.py`.
5. Check it from the repository root: `./check m13l02-05`.

## Expected output

```text
5
True
False
True
```

## How to check

`./check m13l02-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-testing-equality-changes-nothing.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
