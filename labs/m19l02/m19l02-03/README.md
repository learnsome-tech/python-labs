# m19l02-03 · The filtering clause

**Lesson:** [Comprehensions](https://learnsome.tech/learn/python-course/m19l02) (lesson 19.2, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can turn a build-a-list loop into a list comprehension with an optional filter, write dictionary and set comprehensions, and say when a plain loop is the clearer choice.

In the lesson: A comprehension can leave things out, with an if on the end. Take the same four words: upper case them, but only those longer than three letters, and the short one is gone from the result. That is the filtering clause, and it is how you keep the ones you want without an if statement inside a loop. Filtering over a range gives you the multiples of three under twenty. Now look at the last line, because it is a different thing that looks similar. An if in front of the for is a conditional expression choosing between two values, so every item is kept but changed. An if after the for decides whether an item is kept at all. Front chooses, back filters.

## Files

- [`starter/shell-the-filtering-clause.py`](starter/shell-the-filtering-clause.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l02/m19l02-03/starter`
2. Read `shell-the-filtering-clause.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   words = ['pear', 'fig', 'banana', 'kiwi']
   [w.upper() for w in words if len(w) > 3]
   [w for w in words if 'a' in w]
   [x for x in range(20) if x % 3 == 0]
   ['long' if len(w) > 3 else 'short' for w in words]
   ```
4. Run it: `python3 -i < shell-the-filtering-clause.py`.
5. Check it from the repository root: `./check m19l02-03`.

## Expected output

```text
['PEAR', 'BANANA', 'KIWI']
['pear', 'banana']
[0, 3, 6, 9, 12, 15, 18]
['long', 'short', 'long', 'long']
```

## How to check

`./check m19l02-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-filtering-clause.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
