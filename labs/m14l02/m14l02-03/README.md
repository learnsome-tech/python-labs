# m14l02-03 · readLines1.py, ask before every line

**Lesson:** [Interactive While Loops](https://learnsome.tech/learn/python-course/m14l02) (lesson 14.2, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop that reads input until a sentinel value arrives, initialising the test data before the loop and resetting it at the end of the body so the loop can stop.

In the lesson: The user may want to enter a pile of lines without counting them ahead of time, so here a while loop takes over. The obvious, if verbose, way to decide whether to continue is to ask before every line. Look for the two statements that set the test answer: one before the loop, so the first test has something to work with, and one at the bottom of the body, so the next test has fresh data. The lines are printed back at the end as before, and the same loop is shipped inside a function in the example called consent loop dot py. Run it: one line of real data cost two answers. This works, but it may be more annoying than counting ahead.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/readLines1.py`](starter/readLines1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l02/m14l02-03/starter`
2. Read `readLines1.py` the way the lesson builds it:
   - Lines 1–4: one before the loop
   - Lines 5–8: one at the bottom of the body
   - Lines 9–12: printed back at the end
3. Run it: `python3 readLines1.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m14l02-03`.

## Expected output

```text
Press y if you want to enter more lines: Next line: Press y if you want to enter more lines: Your lines were:
tea leaves
```

## How to check

`./check m14l02-03` copies `starter/` into a scratch directory and runs `python3 readLines1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
