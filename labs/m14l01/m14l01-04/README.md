# m14l01-04 · Test yourself: testWhile.py

**Lesson:** [While Loops, And The General Range](https://learnsome.tech/learn/python-course/m14l01) (lesson 14.1, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop whose condition is tested before every pass, spot a loop that will never stop, and use the three argument range function to replace a counting while loop with a for loop.

In the lesson: Test yourself on this one before you run it. Follow the code by hand and work out exactly what is printed. The variable i starts at four, the condition asks whether i is less than nine, and the body prints i and then adds two to it. Four is printed, then six, then eight. When i reaches ten the test fails, so ten is never printed, and notice that nine never appears either, because the steps of two skip straight over it. Now check yourself by running the example program. The numbers on the screen should be the three you predicted.

## Files

- [`starter/testWhile.py`](starter/testWhile.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l01/m14l01-04/starter`
2. Read `testWhile.py`.
3. Run it: `python3 testWhile.py`.
4. Check it from the repository root: `./check m14l01-04`.

## Expected output

```text
4
6
8
```

## How to check

`./check m14l01-04` copies `starter/` into a scratch directory and runs `python3 testWhile.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
