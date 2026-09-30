# m07l04-07 · First attempt: right once, then stuck

**Lesson:** [Repeat Loops And Successive Modification](https://learnsome.tech/learn/python-course/m07l04) (lesson 7.4, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can write a simple repeat loop whose loop variable you never use, and build a loop that modifies a variable of your own on every pass, tracing its value pass by pass.

In the lesson: Here is the first attempt, number entries one. Before the loop I set number to one. Inside the loop I print number and then the item, and the print function puts a space between the two values for me. Run it and you see the same number four times. That is not counting, but it is real progress, because the very first line of output is exactly right. The lesson to take is this: a variable given a value before the loop keeps that value on every single pass, unless something inside the loop changes it.

## Files

- [`starter/numberEntries1.py`](starter/numberEntries1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-07/starter`
2. Read `numberEntries1.py` the way the lesson builds it:
   - Lines 1: number entries one
   - Lines 2–4: I set number to one
   - Lines 5–6: print number and then the item
3. Run it: `python3 numberEntries1.py`.
4. Check it from the repository root: `./check m07l04-07`.

## Expected output

```text
1 red
1 orange
1 yellow
1 green
```

## How to check

`./check m07l04-07` copies `starter/` into a scratch directory and runs `python3 numberEntries1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
