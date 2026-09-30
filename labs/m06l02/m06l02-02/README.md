# m06l02-02 · Two people, two definitions

**Lesson:** [Several Functions, And Flow Of Control](https://learnsome.tech/learn/python-course/m06l02) (lesson 6.2, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can put several function definitions in one file, predict the order in which the lines are executed, and see how indentation decides what is remembered and what is run.

In the lesson: Here is example program birthday four. Above the blank line is the first definition, for Emily, unchanged from last time. Below it is a second definition, for Andre, differing in its name and in one line of the song. Then come the last two lines, which are not indented. Guess what happens, and then try it. Everything in this file is definition except those final two lines, and they are the only lines executed directly. Emily is sung to, then Andre. Notice that the calls happen to be in the same order as the definitions, but that is arbitrary. The definitions fix what the names mean; the calls at the bottom fix what happens and when.

## Files

- [`starter/birthday4.py`](starter/birthday4.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-02/starter`
2. Read `birthday4.py` the way the lesson builds it:
   - Lines 1–7: the first definition
   - Lines 8–13: a second definition
   - Lines 14–16: the last two lines
3. Notes from the lesson:
   - Line 15: the only two lines executed directly
4. Run it: `python3 birthday4.py`.
5. Check it from the repository root: `./check m06l02-02`.

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

`./check m06l02-02` copies `starter/` into a scratch directory and runs `python3 birthday4.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
