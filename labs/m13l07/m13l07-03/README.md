# m13l07-03 · Packing and unpacking a tuple

**Lesson:** [Loops And Tuples](https://learnsome.tech/learn/python-course/m13l07) (lesson 13.7, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can package related values in a tuple, unpack a tuple in a for loop heading, and replace a long repetitive if elif statement with a loop over a list of tuples.

In the lesson: You can reach the parts of a tuple by indexing, but the more common way is multiple assignment. Here is the tutorial's silly simple example. The first line packs the numbers one and two into a tuple called tup. The second line unpacks it again: a tuple of two names on the left is matched piece by piece against the tuple on the right, so x is assigned the first part and y the second. Run it and you see one, then two. The shapes on the two sides must match. Remember this, because the loop we are about to write depends on it.

## Files

- [`starter/tupleAssign.py`](starter/tupleAssign.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l07/m13l07-03/starter`
2. Read `tupleAssign.py` the way the lesson builds it:
   - Lines 1: packs the numbers
   - Lines 2: unpacks it again
   - Lines 3–4: Run it and you see one
3. Run it: `python3 tupleAssign.py`.
4. Check it from the repository root: `./check m13l07-03`.

## Expected output

```text
1
2
```

## How to check

`./check m13l07-03` copies `starter/` into a scratch directory and runs `python3 tupleAssign.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
