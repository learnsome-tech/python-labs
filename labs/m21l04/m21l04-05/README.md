# m21l04-05 · os, sys, subprocess and argparse: talking outwards

**Lesson:** [A Standard Library Tour](https://learnsome.tech/learn/python-course/m21l04) (lesson 21.4, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can name the standard library modules a beginner actually meets, say what each one is for, recognise when a problem belongs to one of them, and look the details up for yourself.

In the lesson: These four are how a program talks to the world outside itself. Argparse turns command line arguments into an object with named attributes, and gives you a help message and error checking free; here I pass a list so the example is repeatable, where normally parse args reads the real command line. Subprocess runs another program and captures what it printed, and you always hand it a list of words rather than one string. The os module covers the operating system: environment variables, directories, and the older path functions that pathlib now mostly replaces. Sys is Python about itself: the argument list, the exit function, the path it searches and the interpreter's own version. Read the four lines of output against the code.

## Files

- [`starter/toolBox.py`](starter/toolBox.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l04/m21l04-05/starter`
2. Read `toolBox.py`.
3. Notes from the lesson:
   - Line 9: normally parse args reads the real command line
   - Line 12: a list of words, never one string, and never the shell
4. Run it: `python3 toolBox.py`.
5. Check it from the repository root: `./check m21l04-05`.

## Expected output

```text
hihihi
0 2
notes.txt
3
```

## How to check

`./check m21l04-05` copies `starter/` into a scratch directory and runs `python3 toolBox.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
