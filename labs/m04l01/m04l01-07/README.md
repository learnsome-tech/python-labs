# m04l01-07 · Negation

**Lesson:** [Integer Arithmetic And Precedence](https://learnsome.tech/learn/python-course/m04l01) (lesson 4.1, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can evaluate integer arithmetic at the Python shell, predict the result from the normal rules of precedence, and recognise a continuation line when a parenthesis is left open.

In the lesson: Negation also works. Put a minus sign in front of a parenthesised expression and Python negates the whole result: two plus three is five, and the negation of that is minus five. So the same minus sign has two jobs. Between two values it means subtraction. In front of a single value it means negation. Python decides which meaning applies from the position of the symbol, and that is a pattern you will meet again with other operators.

## Files

- [`starter/shell-negation.py`](starter/shell-negation.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-07/starter`
2. Read `shell-negation.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   -(2 + 3)
   ```
4. Run it: `python3 -i < shell-negation.py`.
5. Check it from the repository root: `./check m04l01-07`.

## Expected output

```text
-5
```

## How to check

`./check m04l01-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-negation.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
