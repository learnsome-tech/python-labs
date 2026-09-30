# m19l01-03 · Which of them will change under you

**Lesson:** [Lists, Tuples, Sets, Dicts: Choosing One](https://learnsome.tech/learn/python-course/m19l01) (lesson 19.1, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can choose between a list, a tuple, a set and a dictionary for a given job, say what each costs to search, and explain why a tuple can be a dictionary key when a list cannot.

In the lesson: Now the one column that separates a list from a tuple. A list can be changed in place: append, and it is the same list, now longer. A tuple refuses. Assign to one of its positions and Python says a tuple object does not support item assignment. You can add tuples together, but look carefully at what that gives you: a brand new tuple, with the original untouched. That is what immutable means. Adding to a tuple is impossible; building another one from it is easy. And for a set, adding a value it already holds is not an error and not a duplicate: nothing happens at all, and the set is unchanged. That property is why sets are the tool for the word unique.

## Files

- [`starter/shell-which-of-them-will-change-under-you.py`](starter/shell-which-of-them-will-change-under-you.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l01/m19l01-03/starter`
2. Read `shell-which-of-them-will-change-under-you.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   nums = [3, 1, 4]
   nums.append(9)
   nums
   point = (2, 5)
   point[0] = 7
   point + (9,)
   seen = {1, 3, 4}
   seen.add(4)
   seen
   ```
4. Run it: `python3 -i < shell-which-of-them-will-change-under-you.py`.
5. Check it from the repository root: `./check m19l01-03`.

## Expected output

```text
[3, 1, 4, 9]
Traceback (most recent call last):
TypeError: 'tuple' object does not support item assignment
(2, 5, 9)
{1, 3, 4}
```

## How to check

`./check m19l01-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-which-of-them-will-change-under-you.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
