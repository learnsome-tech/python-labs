# m07l05-05 · The whole function, and a test call

**Lesson:** [Accumulation Loops](https://learnsome.tech/learn/python-course/m07l05) (lesson 7.5, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can build a loop that accumulates a result, choose the right initial value for the accumulator, and recognise from an English description when a loop through a sequence is needed.

In the lesson: Here is the whole function, with the return statement added. Look hard at where that return sits. It is outside the loop, lined up with the for heading, so it runs once, after every number has been added. If you indented it into the body by mistake, the function would return after the first number and the rest of the list would be ignored. The example file has a test call at the bottom, not indented, so it runs when the program runs. Run it and eighteen appears, because five and two and four and seven make eighteen.

## Files

- [`starter/sumNums.py`](starter/sumNums.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l05/m07l05-05/starter`
2. Read `sumNums.py` the way the lesson builds it:
   - Lines 1–6: the return statement
   - Lines 7–8: a test call at the bottom
3. Notes from the lesson:
   - Line 6: outside the loop: return only once every number has been added
4. Run it: `python3 sumNums.py`.
5. Check it from the repository root: `./check m07l05-05`.

## Expected output

```text
18
```

## How to check

`./check m07l05-05` copies `starter/` into a scratch directory and runs `python3 sumNums.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
