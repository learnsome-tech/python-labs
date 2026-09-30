# m04l01-02 · Type it and press Enter

**Lesson:** [Integer Arithmetic And Precedence](https://learnsome.tech/learn/python-course/m04l01) (lesson 4.1, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can evaluate integer arithmetic at the Python shell, predict the result from the normal rules of precedence, and recognise a continuation line when a parenthesis is left open.

In the lesson: Start with the number seventy seven on its own. Python evaluates it and prints the value back, and since there is nothing to calculate, the shell appears to echo exactly what you typed. Now try two plus three. The plus sign means what you expect, and the answer five appears on the next line at the left margin. Then try five minus seven. Subtraction works too, and the answer is minus two, so Python is perfectly comfortable with negative results. Notice that you never asked Python to print anything. In the shell, an expression on its own is evaluated and its value is displayed for you.

## Files

- [`starter/shell-type-it-and-press-enter.py`](starter/shell-type-it-and-press-enter.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-02/starter`
2. Read `shell-type-it-and-press-enter.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   77
   2 + 3
   5 - 7
   ```
4. Run it: `python3 -i < shell-type-it-and-press-enter.py`.
5. Check it from the repository root: `./check m04l01-02`.

## Expected output

```text
77
5
-2
```

## How to check

`./check m04l01-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-type-it-and-press-enter.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
