# m04l04-02 · Assignment displays nothing

**Lesson:** [Variables And Assignment](https://learnsome.tech/learn/python-course/m04l04) (lesson 4.4, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write assignment statements, explain why the right hand side is evaluated first, and tell a syntax error apart from a name error found while a line is running.

In the lesson: Try the first line, where width is assigned ten. Nothing is displayed by the interpreter after this entry, so it is not clear anything happened. Something has happened. This is an assignment statement, with a variable, width, on the left. A variable is a name for a value. An assignment statement associates a variable name on the left of the equal sign with the value of an expression calculated from the right of the equal sign. Now type the name on its own and press Enter. Once a variable is assigned a value, the variable can be used in place of that value, so the response is the same as if its value had been entered. The interpreter does not print a value after an assignment statement because the value of the expression on the right is not lost. It can be recovered whenever you like, exactly as we did here.

## Files

- [`starter/shell-assignment-displays-nothing.py`](starter/shell-assignment-displays-nothing.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-02/starter`
2. Read `shell-assignment-displays-nothing.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   width = 10
   width
   ```
4. Run it: `python3 -i < shell-assignment-displays-nothing.py`.
5. Check it from the repository root: `./check m04l04-02`.

## Expected output

```text
10
```

## How to check

`./check m04l04-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-assignment-displays-nothing.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
