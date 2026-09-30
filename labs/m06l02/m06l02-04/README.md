# m06l02-04 · Putting the calls inside a main function

**Lesson:** [Several Functions, And Flow Of Control](https://learnsome.tech/learn/python-course/m06l02) (lesson 6.2, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can put several function definitions in one file, predict the order in which the lines are executed, and see how indentation decides what is remembered and what is run.

In the lesson: Functions you write can also call other functions you write. It is a good convention to have the main action of a program sit inside a function, so a reader can find it. Example program birthday five keeps the two song definitions and adds a third definition, called main, which holds the two Happy Birthday calls. Do you see that this version accomplishes the same thing as the last one? Run it, and it does. If we want the program to do anything at all when it runs, we need one line outside of definitions. The final line is that line, and it is the only one executed directly. It calls the code in main, which in turn calls the code in the other two functions.

## Files

- [`starter/birthday5.py`](starter/birthday5.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-04/starter`
2. Read `birthday5.py` the way the lesson builds it:
   - Lines 1–13: the two song definitions
   - Lines 14–17: a third definition
   - Lines 18–19: one line outside
3. Notes from the lesson:
   - Line 15: main calls the other two functions you wrote
   - Line 19: the only line the interpreter executes directly
4. Run it: `python3 birthday5.py`.
5. Check it from the repository root: `./check m06l02-04`.

## Expected output

```text
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Emily.
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Andre.
Happy Birthday to you!
```

## How to check

`./check m06l02-04` copies `starter/` into a scratch directory and runs `python3 birthday5.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
