# m10l01-10 · Test the function on its own, first

**Lesson:** [Mad Libs Revisited: Finding The Cues](https://learnsome.tech/learn/python-course/m10l01) (lesson 10.1, module 10: Mad Libs Revisited) · Pro  
**Check:** Graded

## Goal

You can write a function that scans a format string and returns the list of cues embedded in it, and you can follow the creative process that produced it.

In the lesson: Because the new part is a function, we can test it on its own without running a whole mad lib program. Here is a scratch file with the function copied in and a single print at the bottom, using the short story we drew the index rows for. Run it, and the answer is a list of two keys, animal and food, in the order they appear. That is what we worked out by hand in the shell, so the loop, the slice and the initial value of end are all behaving. Trying a small piece on small data, where you already know the answer, is how you keep a big program honest.

## Files

- [`starter/tryGetKeys.py`](starter/tryGetKeys.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m10l01/m10l01-10/starter`
2. Read `tryGetKeys.py`.
3. Run it: `python3 tryGetKeys.py`.
4. Check it from the repository root: `./check m10l01-10`.

## Expected output

```text
['animal', 'food']
```

## How to check

`./check m10l01-10` copies `starter/` into a scratch directory and runs `python3 tryGetKeys.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
