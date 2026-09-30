# m14l02-02 · readLines0.py, ask for a count first

**Lesson:** [Interactive While Loops](https://learnsome.tech/learn/python-course/m14l02) (lesson 14.2, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop that reads input until a sentinel value arrives, initialising the test data before the loop and resetting it at the end of the body so the loop can stop.

In the lesson: Here is the first answer, and the weakest. The count is asked for first, converted from digits to a whole number, and then a plain repeat loop reads that many lines and appends each to the list. A second loop prints what was collected, so you can check. Run it. In this recording the answers are fed in from a file rather than typed, so nothing is echoed and the prompts appear run together on one line: the count prompt, two requests for a line, then the heading over the results. The trouble is having to count your lines before you start.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/readLines0.py`](starter/readLines0.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l02/m14l02-02/starter`
2. Read `readLines0.py`.
3. Notes from the lesson:
   - Line 4: the count decides how many times the loop runs
   - Line 5: a plain repeat loop: n passes, no more, no less
4. Run it: `python3 readLines0.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m14l02-02`.

## Expected output

```text
How many lines do you want to enter? Next line: Next line: Your lines were:
tea leaves
hot water
```

## How to check

`./check m14l02-02` copies `starter/` into a scratch directory and runs `python3 readLines0.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
