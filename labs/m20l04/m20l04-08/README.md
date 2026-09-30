# m20l04-08 · dataclass, for the plain data case

**Lesson:** [Dunder Methods, And Making Objects Pythonic](https://learnsome.tech/learn/python-course/m20l04) (lesson 20.4, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can give a class a useful repr and str, define equality and hashing consistently, make an object work with len, indexing and a for loop, and reach for a dataclass when the class is plain data.

In the lesson: Most classes are mostly plumbing: store a few fields, print them, compare them. The dataclass decorator from the dataclasses module writes that plumbing. Put a decorator above the class, then one line per field, giving a name, a type after the colon and an optional default. The decorator writes the initialiser, a repr and an equality method. Look at the generated repr: it names each field, which is a good style to copy when you write one by hand. Equality compares all the fields, so a point built from the same numbers is equal and one with a different second number is not. Reach for a dataclass whenever the class is data with a little behaviour, and write the methods yourself when the behaviour is the point.

## Files

- [`starter/pointData.py`](starter/pointData.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l04/m20l04-08/starter`
2. Read `pointData.py` the way the lesson builds it:
   - Lines 1–5: a decorator above the class
   - Lines 6–8: one line per field
   - Lines 9–14: the generated repr
3. Notes from the lesson:
   - Line 5: @dataclass writes __init__, __repr__ and __eq__ for you
   - Line 8: a type after the colon, and an optional default value
   - Line 11: note the field names in the output: x= and y=
4. Run it: `python3 pointData.py`.
5. Check it from the repository root: `./check m20l04-08`.

## Expected output

```text
Point(x=3, y=0)
True
3 0
False
```

## How to check

`./check m20l04-08` copies `starter/` into a scratch directory and runs `python3 pointData.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
