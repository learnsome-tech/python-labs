# m13l05-06 · Short circuit: the second part may never run

**Lesson:** [Compound Boolean Expressions](https://learnsome.tech/learn/python-course/m13l05) (lesson 13.5, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can build conditions with and, or and not, read their precedence and short circuit behaviour, and return a Boolean expression directly instead of wrapping it in an if else.

In the lesson: Something important is hiding in the second and third lines. Set x to zero, then ask whether x is not zero and something divided by x is big. Dividing by zero would raise an error, yet the shell answers False without complaint. The left part is false, so the answer is already settled and Python never evaluates the right part at all. The same happens with or when the left part is true: one true part is enough, so the rest is skipped. This is short circuit evaluation, and it is what lets you put a safety check on the left of an and and the risky expression on the right.

## Files

- [`starter/shell-short-circuit-the-second-part-may-never-run.py`](starter/shell-short-circuit-the-second-part-may-never-run.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l05/m13l05-06/starter`
2. Read `shell-short-circuit-the-second-part-may-never-run.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   x = 0
   x != 0 and 10 // x > 1
   x == 0 or 10 // x > 1
   not x == 0
   2 < 5 and 3 > 7
   2 < 5 or 3 > 7
   ```
4. Run it: `python3 -i < shell-short-circuit-the-second-part-may-never-run.py`.
5. Check it from the repository root: `./check m13l05-06`.

## Expected output

```text
False
True
False
False
True
```

## How to check

`./check m13l05-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-short-circuit-the-second-part-may-never-run.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
