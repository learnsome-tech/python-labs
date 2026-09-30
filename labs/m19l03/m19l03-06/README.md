# m19l03-06 · Stability: sorting twice on purpose

**Lesson:** [Sorting, Keys And Lambdas](https://learnsome.tech/learn/python-course/m19l03) (lesson 19.3, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can sort anything by any rule using sorted with a key function, write a lambda for that key, and use stability to sort by two rules in turn.

In the lesson: Here is the property that makes sorting genuinely powerful, and it has an ugly name: stability. Python's sort is stable, meaning two items that the key says are equal come out in the order they went in. Nothing is shuffled needlessly. That gives you a trick. To sort by grade, and alphabetically by name within each grade, you do not need a clever key. Sort twice: the less important rule first, then the more important rule last. Run it and look at the second line. Within grade A, Ada comes before Edsger, and within B, Alan before Grace, because the sort by grade left the earlier alphabetical order untouched. Two simple sorts instead of one hard key.

## Files

- [`starter/stability.py`](starter/stability.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l03/m19l03-06/starter`
2. Read `stability.py`.
3. Notes from the lesson:
   - Line 5: least important rule first: by name
   - Line 8: most important rule last: by grade
4. Run it: `python3 stability.py`.
5. Check it from the repository root: `./check m19l03-06`.

## Expected output

```text
[('Ada', 'A'), ('Alan', 'B'), ('Edsger', 'A'), ('Grace', 'B')]
[('Ada', 'A'), ('Edsger', 'A'), ('Alan', 'B'), ('Grace', 'B')]
```

## How to check

`./check m19l03-06` copies `starter/` into a scratch directory and runs `python3 stability.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
