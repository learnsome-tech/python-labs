# m20l04-06 · Putting __hash__ back, consistently

**Lesson:** [Dunder Methods, And Making Objects Pythonic](https://learnsome.tech/learn/python-course/m20l04) (lesson 20.4, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can give a class a useful repr and str, define equality and hashing consistently, make an object work with len, indexing and a for loop, and reach for a dataclass when the class is plain data.

In the lesson: The fix is two lines. Dunder eq is unchanged, and dunder hash returns the hash of the same tuple of coordinates. The rule to obey is that dunder hash must be built from the same data that equality compares, and that data must not change while the object is in a set or used as a key. Three points go into the set and only two come out, because the two equal ones count as one. And you can look one up in a dictionary with a freshly built, equal point. Only do this for objects you treat as values and never modify; for anything you intend to change in place, leave it unhashable and let Python stop you.

## Files

- [`starter/pointHash.py`](starter/pointHash.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l04/m20l04-06/starter`
2. Read `pointHash.py` the way the lesson builds it:
   - Lines 1–12: Dunder eq is unchanged
   - Lines 13–15: hash of the same tuple
   - Lines 16–18: Three points go into the set
3. Notes from the lesson:
   - Line 15: hash the same data that __eq__ compares: that is the rule
   - Line 18: equal keys now find each other in a dictionary
4. Run it: `python3 pointHash.py`.
5. Check it from the repository root: `./check m20l04-06`.

## Expected output

```text
2
home
```

## How to check

`./check m20l04-06` copies `starter/` into a scratch directory and runs `python3 pointHash.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
