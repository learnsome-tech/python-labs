# m04l04-07 · Assignment works the same way with strings

**Lesson:** [Variables And Assignment](https://learnsome.tech/learn/python-course/m04l04) (lesson 4.4, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write assignment statements, explain why the right hand side is evaluated first, and tell a syntax error apart from a name error found while a line is running.

In the lesson: Assignment and variables work equally well with strings. First is assigned the string Sue, last is assigned the string Wong, and then name is assigned first, plus a string holding a single space, plus last. That third line joins the two with a space between them, using the concatenation from the previous module, and it is the first time you have seen variables and an operator working together. Ask for name and the shell shows the string Sue Wong. Nothing new is happening in the rules here. Evaluate the right hand side, whatever its type, then attach the name on the left to the result.

## Files

- [`starter/shell-assignment-works-the-same-way-with-strings.py`](starter/shell-assignment-works-the-same-way-with-strings.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-07/starter`
2. Read `shell-assignment-works-the-same-way-with-strings.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   first = 'Sue'
   last = 'Wong'
   name = first + ' ' + last
   name
   ```
4. Run it: `python3 -i < shell-assignment-works-the-same-way-with-strings.py`.
5. Check it from the repository root: `./check m04l04-07`.

## Expected output

```text
'Sue Wong'
```

## How to check

`./check m04l04-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-assignment-works-the-same-way-with-strings.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
