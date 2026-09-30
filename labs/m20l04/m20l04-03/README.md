# m20l04-03 · __repr__ for the programmer, __str__ for the reader

**Lesson:** [Dunder Methods, And Making Objects Pythonic](https://learnsome.tech/learn/python-course/m20l04) (lesson 20.4, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can give a class a useful repr and str, define equality and hashing consistently, make an object work with len, indexing and a for loop, and reach for a dataclass when the class is plain data.

In the lesson: Here is an ordinary point with two coordinates, and two dunder methods that decide how it appears. Dunder repr comes first, and it is the one for you, the programmer: aim for text a reader could paste back in to rebuild the object. Dunder str is for a human reading output, and print and the str function use it. So the first line is the repr, the next two are the friendly version, once through str and once through print, which reaches for str by itself. The last line is the one worth remembering. Inside a list, Python uses the repr of each element and never the str, which is why a class with a friendly str but no repr still looks useless the moment you print a list of them.

## Files

- [`starter/pointRepr.py`](starter/pointRepr.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l04/m20l04-03/starter`
2. Read `pointRepr.py` the way the lesson builds it:
   - Lines 1–6: an ordinary point
   - Lines 7–9: dunder repr comes first
   - Lines 10–12: Dunder str is for a human
   - Lines 13–18: The first line is the repr
3. Notes from the lesson:
   - Line 9: aim for text a programmer could paste back in to rebuild it
   - Line 12: the friendly form; print and str use this when it exists
   - Line 18: inside a container, repr is used, never str
4. Run it: `python3 pointRepr.py`.
5. Check it from the repository root: `./check m20l04-03`.

## Expected output

```text
Point(1, 2)
the point 1 across, 2 up
the point 1 across, 2 up
[Point(1, 2), Point(3, 4)]
```

## How to check

`./check m20l04-03` copies `starter/` into a scratch directory and runs `python3 pointRepr.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
