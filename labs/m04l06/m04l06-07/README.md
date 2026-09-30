# m04l06-07 · Predict the result

**Lesson:** [The Print Function And String Literals](https://learnsome.tech/learn/python-course/m04l06) (lesson 4.6, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can display anything you like with the print function, write a string literal that spans several lines, and read the escape codes that stand for a newline, a quote or a backslash.

In the lesson: Predict the result, and then try this in the shell. Enter the literal on its own first. It holds three characters of text and three escape codes, all typed on one line, and the shell echoes it back to you exactly as you wrote it, because that is the value. Now print the same literal. Did you guess the right number of lines, splitting in the right places? There are four lines: a, then b, then an empty line, because the two newline codes in the middle sit next to each other with nothing between them, then c. Counting blank lines correctly is a small skill worth having, and it saves you a lot of puzzled staring at output later on.

## Files

- [`starter/shell-predict-the-result.py`](starter/shell-predict-the-result.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l06/m04l06-07/starter`
2. Read `shell-predict-the-result.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   'a\nb\n\nc'
   print('a\nb\n\nc')
   ```
4. Run it: `python3 -i < shell-predict-the-result.py`.
5. Check it from the repository root: `./check m04l06-07`.

## Expected output

```text
'a\nb\n\nc'
a
b

c
```

## How to check

`./check m04l06-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-predict-the-result.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
