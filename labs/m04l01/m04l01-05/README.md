# m04l01-05 · Precedence, and parentheses to override it

**Lesson:** [Integer Arithmetic And Precedence](https://learnsome.tech/learn/python-course/m04l01) (lesson 4.1, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can evaluate integer arithmetic at the Python shell, predict the result from the normal rules of precedence, and recognise a continuation line when a parenthesis is left open.

In the lesson: Now enter two plus three times four. If you expected twenty, think again. The answer is fourteen, because Python uses the normal precedence of arithmetic operations: multiplications and divisions are done before addition and subtraction, unless there are parentheses. If you want the addition to happen first, wrap the addition in parentheses, and the answer becomes twenty. The last line works the same way: the subtraction inside the parentheses is carried out first, giving three, and two times three is six. Parentheses are never wrong to add. Whenever you are not certain of the precedence, put them in, and the person reading your code later will thank you for it.

## Files

- [`starter/shell-precedence-and-parentheses-to-override-it.py`](starter/shell-precedence-and-parentheses-to-override-it.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-05/starter`
2. Read `shell-precedence-and-parentheses-to-override-it.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   2 + 3 * 4
   (2+3)*4
   2 * (4 - 1)
   ```
4. Run it: `python3 -i < shell-precedence-and-parentheses-to-override-it.py`.
5. Check it from the repository root: `./check m04l01-05`.

## Expected output

```text
14
20
6
```

## How to check

`./check m04l01-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-precedence-and-parentheses-to-override-it.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
