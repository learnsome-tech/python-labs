# m17l04-09 · The fix, and the decision inside it

**Lesson:** [Debugging: print, breakpoint, and the debugger](https://learnsome.tech/learn/python-course/m17l04) (lesson 17.4, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can debug a wrong answer deliberately: label your printing, stop a program with breakpoint, step through it with the pdb commands that matter, read the state instead of guessing, and choose between a debugger and a test.

In the lesson: We can now say the fault in one sentence: the starting value was not taken from the data, so a list with no positive numbers in it could never beat the start. The fix follows from that sentence. Begin with the first item of the list, and loop over the rest. Both answers are right now. But look at what the fix assumes: that there is a first item. On an empty list this raises an IndexError, and you have a decision to make of the kind you met earlier in this module. Either refuse the empty list yourself with a raised ValueError and a clear message, or let the IndexError travel. What you should not do is return zero.

## Files

- [`starter/runmaxfixed.py`](starter/runmaxfixed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l04/m17l04-09/starter`
2. Read `runmaxfixed.py`.
3. Run it: `python3 runmaxfixed.py`.
4. Check it from the repository root: `./check m17l04-09`.

## Expected output

```text
9
-2
```

## How to check

`./check m17l04-09` copies `starter/` into a scratch directory and runs `python3 runmaxfixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
