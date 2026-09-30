# m13l01-05 · A simple if statement: suitcase dot py

**Lesson:** [Conditions And Simple If Statements](https://learnsome.tech/learn/python-course/m13l01) (lesson 13.1, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can write a condition, say whether it is True or False, and use a simple if statement to run a block of code only when the condition holds.

In the lesson: Here is the tutorial's first if statement, in the example program suitcase dot py. There is a docstring at the top, then a main function that reads a weight from the user. The middle two lines are the if statement. The heading ends in a colon, and the body is indented under it. Read it as English: if it is true that the weight is greater than fifty, then print the sentence about an extra charge. Below that, the thank you line is not indented under the if, so it always runs. Run it with thirty pounds. Thirty is not greater than fifty, so the condition is False, the indented print is skipped entirely, and all you see is the thank you.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/suitcase.py`](starter/suitcase.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l01/m13l01-05/starter`
2. Read `suitcase.py` the way the lesson builds it:
   - Lines 1–3: a docstring at the top
   - Lines 4–6: reads a weight from the user
   - Lines 7–8: the middle two lines
   - Lines 9–11: the thank you line
3. Notes from the lesson:
   - Line 7: if, then the condition, then a colon
   - Line 8: indented: run only when the condition is True
4. Run it: `python3 suitcase.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m13l01-05`.

## Expected output

```text
How many pounds does your suitcase weigh? Thank you for your business.
```

## How to check

`./check m13l01-05` copies `starter/` into a scratch directory and runs `python3 suitcase.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
