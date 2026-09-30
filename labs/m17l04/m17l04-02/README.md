# m17l04-02 · A function that lies quietly

**Lesson:** [Debugging: print, breakpoint, and the debugger](https://learnsome.tech/learn/python-course/m17l04) (lesson 17.4, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can debug a wrong answer deliberately: label your printing, stop a program with breakpoint, step through it with the pdb commands that matter, read the state instead of guessing, and choose between a debugger and a test.

In the lesson: Here is a function meant to return the largest number in a list. Read it and convince yourself it is right, because most people do. Then run it. The first list gives nine, which is correct. The second answer is wrong. The largest of minus five, minus two and minus nine is minus two, and we are told zero, which is not even in the list. Nothing crashed. If this were buried in a program that printed a total at the end, you might never notice, and that is what makes a wrong answer more dangerous than an exception. Now, resist the urge to guess. Let us find out what the function really does.

## Files

- [`starter/runmax.py`](starter/runmax.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l04/m17l04-02/starter`
2. Read `runmax.py`.
3. Run it: `python3 runmax.py`.
4. Check it from the repository root: `./check m17l04-02`.

## Expected output

```text
9
0
```

## How to check

`./check m17l04-02` copies `starter/` into a scratch directory and runs `python3 runmax.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
