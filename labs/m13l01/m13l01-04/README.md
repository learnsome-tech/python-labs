# m13l01-04 · Proving the difference in the shell

**Lesson:** [Conditions And Simple If Statements](https://learnsome.tech/learn/python-course/m13l01) (lesson 13.1, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can write a condition, say whether it is True or False, and use a simple if statement to run a block of code only when the condition holds.

In the lesson: Here we ask for the type of the quoted version, and Python answers with the class str. Then we compare the two for equality, and the answer is False, because a Boolean value and a string are not the same kind of thing at all. Last, we ask for the type of a comparison, and there is bool again. That is the point worth keeping: any comparison you write, however complicated it later becomes, evaluates to one of those two Boolean values and nothing else.

## Files

- [`starter/shell-proving-the-difference-in-the-shell.py`](starter/shell-proving-the-difference-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l01/m13l01-04/starter`
2. Read `shell-proving-the-difference-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   type('True')
   True == 'True'
   type(2 < 5)
   ```
4. Run it: `python3 -i < shell-proving-the-difference-in-the-shell.py`.
5. Check it from the repository root: `./check m13l01-04`.

## Expected output

```text
<class 'str'>
False
<class 'bool'>
```

## How to check

`./check m13l01-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-proving-the-difference-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
