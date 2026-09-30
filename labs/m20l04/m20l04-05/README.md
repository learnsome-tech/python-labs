# m20l04-05 · __eq__, and what defining it costs you

**Lesson:** [Dunder Methods, And Making Objects Pythonic](https://learnsome.tech/learn/python-course/m20l04) (lesson 20.4, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can give a class a useful repr and str, define equality and hashing consistently, make an object work with len, indexing and a for loop, and reach for a dataclass when the class is plain data.

In the lesson: By default two objects are equal only when they are the very same object, which is rarely what you want for something like a point. Dunder eq fixes that: compare the pair of coordinates and return the answer. Now two separately built points are equal, while is is still about identity and says false, and the in operator uses equality, so it finds a matching point in a list. But there is a price, and it surprises people. When you define dunder eq, Python takes hashability away, because two objects that are equal must hash the same, and Python cannot guess your rule. So putting one in a set, or using one as a dictionary key, now fails with a type error.

## Files

- [`starter/pointEq.py`](starter/pointEq.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l04/m20l04-05/starter`
2. Read `pointEq.py` the way the lesson builds it:
   - Lines 1–12: compare the pair of coordinates
   - Lines 13–17: the in operator uses equality
   - Lines 18–21: putting one in a set
3. Notes from the lesson:
   - Line 12: compare the data, not the identity: two points, one value
   - Line 16: == is now about value; is is still about identity
   - Line 19: defining __eq__ sets __hash__ to None unless you say otherwise
4. Run it: `python3 pointEq.py`.
5. Check it from the repository root: `./check m20l04-05`.

## Expected output

```text
True False
True
TypeError: cannot use 'Point' as a set element (unhashable type: 'Point')
```

## How to check

`./check m20l04-05` copies `starter/` into a scratch directory and runs `python3 pointEq.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
