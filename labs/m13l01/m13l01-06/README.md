# m13l01-06 · The same program with a heavier suitcase

**Lesson:** [Conditions And Simple If Statements](https://learnsome.tech/learn/python-course/m13l01) (lesson 13.1, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can write a condition, say whether it is True or False, and use a simple if statement to run a block of code only when the condition holds.

In the lesson: Not one character of the program has changed. Run it again, and this time answer fifty five. Now the condition is true, so the indented print does run, and you get the extra charge line before the thank you. That is the whole behaviour of a simple if statement: the indented block either runs once or does not run at all, and either way the program carries on with the next line that is not indented under the if. Try it yourself with a weight of exactly fifty pounds, and think carefully about which answer greater than gives you at the boundary.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/suitcase.py`](starter/suitcase.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l01/m13l01-06/starter`
2. Read `suitcase.py`.
3. Run it: `python3 suitcase.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m13l01-06`.

## Expected output

```text
How many pounds does your suitcase weigh? There is a $25 charge for luggage that heavy.
Thank you for your business.
```

## How to check

`./check m13l01-06` copies `starter/` into a scratch directory and runs `python3 suitcase.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
