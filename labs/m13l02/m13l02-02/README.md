# m13l02-02 · clothes dot py, on a cool day

**Lesson:** [If Else, And Conditional Expressions](https://learnsome.tech/learn/python-course/m13l02) (lesson 13.2, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can choose between two blocks of code with an if else statement, write any of the six comparisons correctly, and test membership in a sequence with in and not in.

In the lesson: The example program clothes dot py reads a temperature, then recommends what to wear. Look at the four lines in the middle. First the if heading and its block, which prints the advice for a warm day. Then the else heading and its block, for a cool one. Now look at the last line of main. It is dedented: it lines up with the if, so it is not part of the if else statement, and it runs after whichever block was chosen. Run it and answer fifty. Fifty is not greater than seventy, so the else block runs.

## Files

- [`starter/clothes.py`](starter/clothes.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l02/m13l02-02/starter`
2. Read `clothes.py` the way the lesson builds it:
   - Lines 1–4: reads a temperature
   - Lines 5–6: the if heading and its block
   - Lines 7–8: the else heading and its block
   - Lines 9–11: the last line of main
3. Notes from the lesson:
   - Line 9: dedented, so not part of the if-else: this line always runs
4. Run it: `python3 clothes.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m13l02-02`.

## Expected output

```text
What is the temperature? Wear long pants.
Get some exercise outside.
```

## How to check

`./check m13l02-02` copies `starter/` into a scratch directory and runs `python3 clothes.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
