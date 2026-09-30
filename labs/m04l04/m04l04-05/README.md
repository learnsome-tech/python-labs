# m04l04-05 · Reversed, it is a syntax error

**Lesson:** [Variables And Assignment](https://learnsome.tech/learn/python-course/m04l04) (lesson 4.4, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write assignment statements, explain why the right hand side is evaluated first, and tell a syntax error apart from a name error found while a line is running.

In the lesson: The difference from the mathematical usage can be illustrated. Having assigned ten to width, write the same equation the other way round, with the number on the left. In mathematics those two lines say the same thing. In Python this is not equivalent to the first line at all. The left hand side must be a variable, to which the assignment is made. Reversed, we get a syntax error, because a literal value is not something you can assign to. Read the message Python gives you as well. The modern interpreter guesses that you might have meant the doubled equal sign, which is the test for equality rather than an assignment, and we shall meet that when we come to conditions.

## Files

- [`starter/shell-reversed-it-is-a-syntax-error.py`](starter/shell-reversed-it-is-a-syntax-error.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-05/starter`
2. Read `shell-reversed-it-is-a-syntax-error.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   width = 10
   10 = width
   ```
4. Run it: `python3 -i < shell-reversed-it-is-a-syntax-error.py`.
5. Check it from the repository root: `./check m04l04-05`.

## Expected output

```text
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```

## How to check

`./check m04l04-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-reversed-it-is-a-syntax-error.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
