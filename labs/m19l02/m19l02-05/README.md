# m19l02-05 · Nesting, and flattening

**Lesson:** [Comprehensions](https://learnsome.tech/learn/python-course/m19l02) (lesson 19.2, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can turn a build-a-list loop into a list comprehension with an optional filter, write dictionary and set comprehensions, and say when a plain loop is the clearer choice.

In the lesson: Comprehensions can nest, in two different ways that people confuse. Two for clauses in one comprehension flatten: read them left to right in the order you would have nested them, so for each row, for each value in that row, and out comes one flat list. A comprehension inside a comprehension, with its own brackets, gives you a list of lists, and here that is a multiplication table. Two for clauses over different sources give you every combination, which is a useful trick for pairs. Run it and check each of the three against what you predicted. If you predicted the first one the other way round, you are in good company; that reading order catches everybody once.

## Files

- [`starter/nested.py`](starter/nested.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l02/m19l02-05/starter`
2. Read `nested.py`.
3. Notes from the lesson:
   - Line 5: two fors, left to right, same order as the nested loop
   - Line 8: a comprehension inside a comprehension: a list of lists
4. Run it: `python3 nested.py`.
5. Check it from the repository root: `./check m19l02-05`.

## Expected output

```text
[1, 2, 3, 4, 5, 6]
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
[('a', 1), ('a', 2), ('b', 1), ('b', 2)]
```

## How to check

`./check m19l02-05` copies `starter/` into a scratch directory and runs `python3 nested.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
