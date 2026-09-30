# m13l03-05 · grade one dot py, run for real

**Lesson:** [If Elif Chains](https://learnsome.tech/learn/python-course/m13l03) (lesson 13.3, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can write an if elif else chain to sort a value into any number of cases, and explain why only the first true test matters.

In the lesson: This is the whole example program: the function you have just read, plus a small main function that asks for a numerical grade, calls the function and prints the letter. Enter eighty five. The first test fails, the second succeeds, and the answer is B. Now go and test it properly. Try a score above ninety, one in each band, and something below sixty. Most of all, test the cut off points themselves. What does the chain do with exactly eighty, and what does it do with a score of seventy nine point six? Those boundaries are where grading programs go wrong.

## Files

- [`starter/grade1.py`](starter/grade1.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l03/m13l03-05/starter`
2. Read `grade1.py` the way the lesson builds it:
   - Lines 1–14: the function you have just read
   - Lines 15–21: a small main function
3. Run it: `python3 grade1.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m13l03-05`.

## Expected output

```text
Enter a numerical grade: Your grade is B.
```

## How to check

`./check m13l03-05` copies `starter/` into a scratch directory and runs `python3 grade1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
