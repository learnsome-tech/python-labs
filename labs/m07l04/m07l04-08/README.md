# m07l04-08 · Second attempt: a fixed value works once

**Lesson:** [Repeat Loops And Successive Modification](https://learnsome.tech/learn/python-course/m07l04) (lesson 7.4, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can write a simple repeat loop whose loop variable you never use, and build a loop that modifies a variable of your own on every pass, tracing its value pass by pass.

In the lesson: The idea in number entries two is to change number after printing it, so that it is ready for the next pass. The added last line of the body sets number to two. Run it and the first two lines are right at last, but from there it sticks at two forever. Assigning one particular value can only ever be correct once. What we need is a rule that works on every pass, rather than a value that happens to suit the second pass. Say the counting pattern out loud and the rule appears: each successive number is one more than the previous number.

## Files

- [`starter/numberEntries2.py`](starter/numberEntries2.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-08/starter`
2. Read `numberEntries2.py` the way the lesson builds it:
   - Lines 1–6: number entries two
   - Lines 7: The added last line
3. Run it: `python3 numberEntries2.py`.
4. Check it from the repository root: `./check m07l04-08`.

## Expected output

```text
1 red
2 orange
2 yellow
2 green
```

## How to check

`./check m07l04-08` copies `starter/` into a scratch directory and runs `python3 numberEntries2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
