# m04l04-08 · A name error, found while the line runs

**Lesson:** [Variables And Assignment](https://learnsome.tech/learn/python-course/m04l04) (lesson 4.4, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write assignment statements, explain why the right hand side is evaluated first, and tell a syntax error apart from a name error found while a line is running.

In the lesson: Assign the string Sue again, and then try first is assigned fred, without any quotes around it. Note the different form of the error message. The earlier errors in these tutorials were syntax errors: errors in translation of the instruction. In this last case the syntax was legal, so the interpreter went on to execute the instruction. Only then did it find the error described. There are no quotes around fred, so the interpreter assumed fred was an identifier, but the name fred was not defined at the time the line was executed. It is both easy to forget quotes where you need them for a literal string, and to mistakenly put them around a variable name that should not have them. Now assign the string Frederick to fred, and the very same line makes sense. Ask for first and you get Frederick.

## Files

- [`starter/shell-a-name-error-found-while-the-line-runs.py`](starter/shell-a-name-error-found-while-the-line-runs.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-08/starter`
2. Read `shell-a-name-error-found-while-the-line-runs.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   first = 'Sue'
   first = fred
   fred = 'Frederick'
   first = fred
   first
   ```
4. Run it: `python3 -i < shell-a-name-error-found-while-the-line-runs.py`.
5. Check it from the repository root: `./check m04l04-08`.

## Expected output

```text
Traceback (most recent call last):
NameError: name 'fred' is not defined
'Frederick'
```

## How to check

`./check m04l04-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-a-name-error-found-while-the-line-runs.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
