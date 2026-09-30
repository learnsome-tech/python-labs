# m03l02-04 · Your first line at the prompt

**Lesson:** [Idle And The Python Shell](https://learnsome.tech/learn/python-course/m03l02) (lesson 3.2, module 3: Meet Idle And The Shell) · Pro  
**Check:** Graded

## Goal

You can start Idle, tell the Edit window from the Python Shell window, open a shell from the Run menu, and read a shell transcript, knowing which lines you typed and which the computer answered.

In the lesson: Either initially, or after explicitly opening it, you should now see the Python Shell window. In the shell, the last line shows the triple angle bracket prompt. Those three characters are the prompt, telling you that Idle is waiting for you to type something. Continuing on that same line, enter six plus three, and be sure to end with the Enter or Return key. The shell evaluates the line you entered and prints the result. You can see that Python does arithmetic. Now look carefully at the layout on screen. The result line, showing nine, is produced by the computer, and it does not start with the triple angle bracket prompt. It sits at the left margin instead. That difference is how you tell, at a glance, what you typed from what the computer answered. At the end you see a further prompt, where you can enter your next line.

## Files

- [`starter/shell-your-first-line-at-the-prompt.py`](starter/shell-your-first-line-at-the-prompt.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-04/starter`
2. Read `shell-your-first-line-at-the-prompt.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   6+3
   ```
4. Run it: `python3 -i < shell-your-first-line-at-the-prompt.py`.
5. Check it from the repository root: `./check m03l02-04`.

## Expected output

```text
9
```

## How to check

`./check m03l02-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-your-first-line-at-the-prompt.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
