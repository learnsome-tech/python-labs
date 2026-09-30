# m19l02-02 · The loop and the comprehension, together

**Lesson:** [Comprehensions](https://learnsome.tech/learn/python-course/m19l02) (lesson 19.2, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can turn a build-a-list loop into a list comprehension with an optional filter, write dictionary and set comprehensions, and say when a plain loop is the clearer choice.

In the lesson: Here they are in one program, so you can see they really are the same. The loop first, building the list an item at a time. The comprehension underneath, in a single line. Run it and the two lines agree. Learn the shape by its order: expression first, then the word for, then the source. That is backwards from the loop, where the for comes first, and getting used to that is the only hard part. The brackets tell you the type you get: square brackets give you a list, and there is no version of this that changes the original. A comprehension always builds something new and leaves its source alone.

## Files

- [`starter/lengths.py`](starter/lengths.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l02/m19l02-02/starter`
2. Read `lengths.py` the way the lesson builds it:
   - Lines 1–7: the loop first
   - Lines 8–10: the comprehension underneath
3. Notes from the lesson:
   - Line 10: expression first, then for, then the source
4. Run it: `python3 lengths.py`.
5. Check it from the repository root: `./check m19l02-02`.

## Expected output

```text
[4, 3, 6, 4]
[4, 3, 6, 4]
```

## How to check

`./check m19l02-02` copies `starter/` into a scratch directory and runs `python3 lengths.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
