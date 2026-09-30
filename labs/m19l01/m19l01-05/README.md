# m19l01-05 · What searching costs

**Lesson:** [Lists, Tuples, Sets, Dicts: Choosing One](https://learnsome.tech/learn/python-course/m19l01) (lesson 19.1, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can choose between a list, a tuple, a set and a dictionary for a given job, say what each costs to search, and explain why a tuple can be a dictionary key when a list cannot.

In the lesson: The fast and slow column deserves proof, so time both of them. Two hundred thousand numbers in a list and the same numbers in a set, and the question is whether the last one is present. Asking a list has to walk the list, comparing item by item, so the cost grows with the length. A set computes where the value would be from the value itself and looks in that one place, so the cost does not grow at all. The program prints two answers, both true: the set was faster, and faster by more than a hundred times. The same is true of a dictionary key. That is why searching a long list inside a loop is the single most common reason a beginner's program is slow.

## Files

- [`starter/lookupcost.py`](starter/lookupcost.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l01/m19l01-05/starter`
2. Read `lookupcost.py`.
3. Notes from the lesson:
   - Line 6: the list has to walk every item until it finds one
   - Line 7: the set computes where the value would be and looks there
4. Run it: `python3 lookupcost.py`.
5. Check it from the repository root: `./check m19l01-05`.

## Expected output

```text
the set answered faster: True
by a factor of more than a hundred: True
```

## How to check

`./check m19l01-05` copies `starter/` into a scratch directory and runs `python3 lookupcost.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
