# m13l01-02 · Six comparisons in the shell

**Lesson:** [Conditions And Simple If Statements](https://learnsome.tech/learn/python-course/m13l01) (lesson 13.1, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can write a condition, say whether it is True or False, and use a simple if statement to run a block of code only when the condition holds.

In the lesson: Type each of these lines separately in the shell and predict the answer before you press return. Two less than five is a true statement, so Python prints True. Three greater than seven is not, so you get False. Now assign eleven to x. The shell prints nothing back at all, because an assignment is a statement, not an expression with a value to show you. Ask whether x is greater than ten, and the answer is True. Ask whether two times x is less than x, and with x holding eleven that is False. Finally ask Python for the type of True, and it reports the class bool. Notice the capital letters. Python is case sensitive here, and a lower case true is not a value at all.

## Files

- [`starter/shell-six-comparisons-in-the-shell.py`](starter/shell-six-comparisons-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l01/m13l01-02/starter`
2. Read `shell-six-comparisons-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   2 < 5
   3 > 7
   x = 11
   x > 10
   2 * x < x
   type(True)
   ```
4. Run it: `python3 -i < shell-six-comparisons-in-the-shell.py`.
5. Check it from the repository root: `./check m13l01-02`.

## Expected output

```text
True
False
True
False
<class 'bool'>
```

## How to check

`./check m13l01-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-six-comparisons-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
