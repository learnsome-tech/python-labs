# m04l04-03 · Building a calculation out of variables

**Lesson:** [Variables And Assignment](https://learnsome.tech/learn/python-course/m04l04) (lesson 4.4, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write assignment statements, explain why the right hand side is evaluated first, and tell a syntax error apart from a name error found while a line is running.

In the lesson: Try each of the following lines. Width is assigned ten, then height is assigned twelve, and then area is assigned width times height. The shell says nothing after any of those three, which is exactly what you should expect by now. Ask for area on its own and Python answers one hundred and twenty. Look at what the third line did. The names width and height each stood in place of their values, the multiplication was carried out on those values, and the result was given a name of its own. That is the shape of almost every calculation you will write from here on. Name the inputs, combine them, name the result.

## Files

- [`starter/shell-building-a-calculation-out-of-variables.py`](starter/shell-building-a-calculation-out-of-variables.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-03/starter`
2. Read `shell-building-a-calculation-out-of-variables.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   width = 10
   height = 12
   area = width * height
   area
   ```
4. Run it: `python3 -i < shell-building-a-calculation-out-of-variables.py`.
5. Check it from the repository root: `./check m04l04-03`.

## Expected output

```text
120
```

## How to check

`./check m04l04-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-building-a-calculation-out-of-variables.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
