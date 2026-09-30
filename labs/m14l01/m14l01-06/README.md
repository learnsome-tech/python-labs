# m14l01-06 · testWhile3.py, collecting the numbers

**Lesson:** [While Loops, And The General Range](https://learnsome.tech/learn/python-course/m14l01) (lesson 14.1, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop whose condition is tested before every pass, spot a loop that will never stop, and use the three argument range function to replace a counting while loop with a for loop.

In the lesson: Predict what happens in this related little program. It starts with an empty list and a counter set to four, and the body appends instead of printing, so the numbers are collected rather than shown one by one. Only after the loop has finished does it print the whole list. Run it and you get a list of three numbers, four, six and eight, printed the way Python shows lists, in square brackets and separated by commas. So the loop is an accumulation loop with a while heading instead of a for heading. Keep those three numbers in mind, because there is a much simpler way to generate that sequence.

## Files

- [`starter/testWhile3.py`](starter/testWhile3.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l01/m14l01-06/starter`
2. Read `testWhile3.py` the way the lesson builds it:
   - Lines 1–4: an empty list and a counter
   - Lines 5–7: appends instead of printing
   - Lines 8: Run it
3. Run it: `python3 testWhile3.py`.
4. Check it from the repository root: `./check m14l01-06`.

## Expected output

```text
[4, 6, 8]
```

## How to check

`./check m14l01-06` copies `starter/` into a scratch directory and runs `python3 testWhile3.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
