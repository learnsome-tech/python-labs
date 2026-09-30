# m05l01-06 · Running your saved program

**Lesson:** [The Idle Editor And Running Programs](https://learnsome.tech/learn/python-course/m05l01) (lesson 5.1, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can open, write, save and run a Python program file in the Idle editor, and you can tell program code apart from Shell text.

In the lesson: Your text is colour coded already. Now that you have a complete, saved program, choose Run, then Run Module. The program runs in the Python Shell window, and there is the greeting. Unlike your work in the Shell, this code is saved to a file in your Python folder, so you can open and execute it whenever you want. Note the word module in that menu item: to the interpreter your program file is a module, and we will use that general term from now on. This tutorial assumes programs are run in Idle, though a console or another environment is fine.

## Files

- [`starter/hello.py`](starter/hello.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-06/starter`
2. Read `hello.py`.
3. Run it: `python3 hello.py`.
4. Check it from the repository root: `./check m05l01-06`.

## Expected output

```text
Hello world!
```

## How to check

`./check m05l01-06` copies `starter/` into a scratch directory and runs `python3 hello.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
