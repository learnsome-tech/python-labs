# m17l04-03 · Printing, done properly

**Lesson:** [Debugging: print, breakpoint, and the debugger](https://learnsome.tech/learn/python-course/m17l04) (lesson 17.4, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can debug a wrong answer deliberately: label your printing, stop a program with breakpoint, step through it with the pdb commands that matter, read the state instead of guessing, and choose between a debugger and a test.

In the lesson: The cheapest tool first, used with a little care. Put one print inside the loop, and label both values with their names, because a column of bare numbers tells you nothing an hour later. Print inside the loop, not before it, so you see every pass. Run it: three lines and the answer. Now read them instead of skimming. The variable holding the best value is zero on every single pass, so the assignment inside the condition never happened once. The condition is asking whether the value is greater than zero, and no negative number ever is. There is the bug, in plain sight: the starting value of zero was a guess, and it is not a member of the data.

## Files

- [`starter/runmaxprint.py`](starter/runmaxprint.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l04/m17l04-03/starter`
2. Read `runmaxprint.py`.
3. Notes from the lesson:
   - Line 4: label every value you print, and print it inside the loop
4. Run it: `python3 runmaxprint.py`.
5. Check it from the repository root: `./check m17l04-03`.

## Expected output

```text
value is -5 and best is 0
value is -2 and best is 0
value is -9 and best is 0
0
```

## How to check

`./check m17l04-03` copies `starter/` into a scratch directory and runs `python3 runmaxprint.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
