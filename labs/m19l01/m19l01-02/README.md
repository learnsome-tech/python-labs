# m19l01-02 · Making all four, and reaching in

**Lesson:** [Lists, Tuples, Sets, Dicts: Choosing One](https://learnsome.tech/learn/python-course/m19l01) (lesson 19.1, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can choose between a list, a tuple, a set and a dictionary for a given job, say what each costs to search, and explain why a tuple can be a dictionary key when a list cannot.

In the lesson: Build one of each in the Shell. A list keeps them in order, exactly as written, and you reach one by position with square brackets. A tuple uses round brackets and looks the same from outside. A set is braces with no colons, and look what happened: one of the two ones is gone, and the numbers came back in a different order from the one you typed. Both of those are the point of a set. It holds each value once, and it does not keep an order, so never rely on how it prints. A dictionary is braces with colons, pairs of key and value, and you reach a value by its key rather than by position.

## Files

- [`starter/shell-making-all-four-and-reaching-in.py`](starter/shell-making-all-four-and-reaching-in.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l01/m19l01-02/starter`
2. Read `shell-making-all-four-and-reaching-in.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   nums = [3, 1, 4, 1, 5]
   nums[0]
   point = (2, 5)
   seen = {3, 1, 4, 1, 5}
   seen
   len(seen)
   ages = {'ada': 36, 'alan': 41}
   ages['ada']
   type(nums)
   ```
4. Run it: `python3 -i < shell-making-all-four-and-reaching-in.py`.
5. Check it from the repository root: `./check m19l01-02`.

## Expected output

```text
3
{1, 3, 4, 5}
4
36
<class 'list'>
```

## How to check

`./check m19l01-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-making-all-four-and-reaching-in.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
