# m14l02-06 · readLines2.py, an empty line to quit

**Lesson:** [Interactive While Loops](https://learnsome.tech/learn/python-course/m14l02) (lesson 14.2, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop that reads input until a sentinel value arrives, initialising the test data before the loop and resetting it at the end of the body so the loop can stop.

In the lesson: Here is that idea as a program. Two print statements tell the user the rule, since a sentinel only works if the user knows about it. Then the same discipline as before: the variable line is set before the loop and at the end of the body, and the heading continues for as long as the line is not empty. Notice the comments the author left on those two lines; the second one is the one people forget. Run it. Two lines of data and one empty line, and both lines come back. One extra keystroke ends the input, no matter how much data you have.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/readLines2.py`](starter/readLines2.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l02/m14l02-06/starter`
2. Read `readLines2.py` the way the lesson builds it:
   - Lines 1–6: tell the user the rule
   - Lines 7–11: before the loop and at the end of the body
   - Lines 12–15: Run it
3. Run it: `python3 readLines2.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m14l02-06`.

## Expected output

```text
Enter lines of text.
Enter an empty line to quit.
Next line: Next line: Next line: Your lines were:
tea leaves
hot water
```

## How to check

`./check m14l02-06` copies `starter/` into a scratch directory and runs `python3 readLines2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
