# m04l06-04 · Triple quoted string literals

**Lesson:** [The Print Function And String Literals](https://learnsome.tech/learn/python-course/m04l06) (lesson 4.6, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can display anything you like with the print function, write a string literal that spans several lines, and read the escape codes that stand for a newline, a quote or a backslash.

In the lesson: Strings delimited by one quote character are required to lie within a single Python line. It is sometimes convenient to have a multi-line string, which can be delimited with triple quotes: three single quote characters in a row. Type the assignment on the screen. You will get continuation lines until the closing triple quotes. Then print it. The line structure is preserved in a multi-line string, so what you typed on three lines comes back on three lines, and as you can see, this also allows you to embed both single and double quote characters. Now enter just the variable name, with no print call. The answer looks strange. All three lines have come back as one line, in single quotes, with a backslash and an n wherever a line break was, and a backslash before the apostrophe.

## Files

- [`starter/shell-triple-quoted-string-literals.py`](starter/shell-triple-quoted-string-literals.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l06/m04l06-04/starter`
2. Read `shell-triple-quoted-string-literals.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   sillyTest = '''Say,
   "I'm in!"
   This is line 3'''
   print(sillyTest)
   sillyTest
   ```
4. Run it: `python3 -i < shell-triple-quoted-string-literals.py`.
5. Check it from the repository root: `./check m04l06-04`.

## Expected output

```text
Say,
"I'm in!"
This is line 3
'Say,\n"I\'m in!"\nThis is line 3'
```

## How to check

`./check m04l06-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-triple-quoted-string-literals.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
