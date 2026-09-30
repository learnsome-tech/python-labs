# m05l01-08 · The same line typed in the Shell

**Lesson:** [The Idle Editor And Running Programs](https://learnsome.tech/learn/python-course/m05l01) (lesson 5.1, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can open, write, save and run a Python program file in the Idle editor, and you can tell program code apart from Shell text.

In the lesson: You could also have typed that single printing line directly in the Shell, in response to a Shell prompt. Here it is: the print function on the line you type, and the greeting on the next line. That is a conversation, not something you could save in a file and run. The same line, with no prompt in front of it, entered into an edit window, is a program you can save and run. Soon we get to many-statement programs, where the edit window is far more convenient.

## Files

- [`starter/shell-the-same-line-typed-in-the-shell.py`](starter/shell-the-same-line-typed-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-08/starter`
2. Read `shell-the-same-line-typed-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   print('Hello world!')
   ```
4. Run it: `python3 -i < shell-the-same-line-typed-in-the-shell.py`.
5. Check it from the repository root: `./check m05l01-08`.

## Expected output

```text
Hello world!
```

## How to check

`./check m05l01-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-same-line-typed-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
