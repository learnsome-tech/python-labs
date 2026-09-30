# m01l04-03 · The same four lines, in a file

**Lesson:** [Editors, IDEs And Shells](https://learnsome.tech/learn/python-course/m01l04) (lesson 1.4, module 1: Before You Write Code) · Free  
**Check:** Graded

## Goal

You can tell a terminal, a shell and a Python shell apart, choose between an interactive shell, an editor with a terminal, and an IDE for a given piece of work, and say what Idle gives you and when to move on from it.

In the lesson: Now put those very same lines into a file and run the file. The result is a shock the first time. The first two lines are calculated exactly as before, and their values are thrown away without a word, because a file is not having a conversation with you. Only the last line, the one that calls print, puts anything on your screen, and the answer is twenty. That is the rule to carry with you: in a file, nothing appears unless you ask for it. The shell volunteers answers because you are sitting there waiting for them. A program is silent by default, and print is how you break the silence. Run the file yourself and watch three quarters of it disappear.

## Files

- [`starter/first_program.py`](starter/first_program.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-03/starter`
2. Read `first_program.py` the way the lesson builds it:
   - Lines 1–2: the first two lines
   - Lines 3–4: only the last line
3. Run it: `python3 first_program.py`.
4. Check it from the repository root: `./check m01l04-03`.

## Expected output

```text
20
```

## How to check

`./check m01l04-03` copies `starter/` into a scratch directory and runs `python3 first_program.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
