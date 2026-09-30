# m13l02-03 · The same program on a warm day

**Lesson:** [If Else, And Conditional Expressions](https://learnsome.tech/learn/python-course/m13l02) (lesson 13.2, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can choose between two blocks of code with an if else statement, write any of the six comparisons correctly, and test membership in a sequence with in and not in.

In the lesson: Run the identical program again and answer eighty this time. The condition is true, so the first block runs and the second is skipped. Only one clothing recommendation is ever printed, which is what you want. The advice about exercise appears in both runs, because that line is not part of the if else statement. Had you indented it under the else by mistake, you would hear about exercise only on cool days.

## Files

- [`starter/clothes.py`](starter/clothes.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l02/m13l02-03/starter`
2. Read `clothes.py`.
3. Run it: `python3 clothes.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m13l02-03`.

## Expected output

```text
What is the temperature? Wear shorts.
Get some exercise outside.
```

## How to check

`./check m13l02-03` copies `starter/` into a scratch directory and runs `python3 clothes.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
