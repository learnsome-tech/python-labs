# m04l01-04 · Python does not use x for multiplication

**Lesson:** [Integer Arithmetic And Precedence](https://learnsome.tech/learn/python-course/m04l01) (lesson 4.1, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can evaluate integer arithmetic at the Python shell, predict the result from the normal rules of precedence, and recognise a continuation line when a parenthesis is left open.

In the lesson: Try two x three. You should get your first syntax error. The letter x becomes highlighted, indicating the location where the Python interpreter discovered that it cannot understand you. Python does not use x for multiplication as you may have done in grade school, because x is far too useful as a variable name, and the two uses would be confused. Instead the symbol for multiplication is an asterisk. Type two asterisk five and Python answers ten. Now type the same thing with spaces around it. You get ten again. The interpreter can figure out what you mean either way, so the spaces are optional, though a space can make understanding quicker for a human reader.

## Files

- [`starter/shell-python-does-not-use-x-for-multiplication.py`](starter/shell-python-does-not-use-x-for-multiplication.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-04/starter`
2. Read `shell-python-does-not-use-x-for-multiplication.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   2 x 3
   2*5
   2 * 5
   ```
4. Run it: `python3 -i < shell-python-does-not-use-x-for-multiplication.py`.
5. Check it from the repository root: `./check m04l01-04`.

## Expected output

```text
SyntaxError: invalid syntax
10
10
```

## How to check

`./check m04l01-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-python-does-not-use-x-for-multiplication.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
