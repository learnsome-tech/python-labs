# m19l01-06 · Why a tuple can be a key and a list cannot

**Lesson:** [Lists, Tuples, Sets, Dicts: Choosing One](https://learnsome.tech/learn/python-course/m19l01) (lesson 19.1, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can choose between a list, a tuple, a set and a dictionary for a given job, say what each costs to search, and explain why a tuple can be a dictionary key when a list cannot.

In the lesson: This explains the fast column, and one error you are certain to meet. Start with an empty dictionary and use a pair of coordinates as the key. It works, and it reads back perfectly. Try the same thing with a list of two numbers and Python refuses: it cannot use a list as a dictionary key, because a list is unhashable. Here is why. To find a key quickly, Python turns it into a number, its hash, and remembers where it filed it. That only works if the hash gives the same answer every time. A tuple cannot change, so it cannot; a list can be appended to at any moment, and the dictionary would lose track of it. Immutable values can be keys and set members. Mutable ones cannot. You can still sort the keys when you want an order.

## Files

- [`starter/shell-why-a-tuple-can-be-a-key-and-a-list-cannot.py`](starter/shell-why-a-tuple-can-be-a-key-and-a-list-cannot.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l01/m19l01-06/starter`
2. Read `shell-why-a-tuple-can-be-a-key-and-a-list-cannot.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   grid = {}
   grid[(0, 0)] = 'start'
   grid[(2, 3)] = 'treasure'
   grid[(0, 0)]
   grid[[0, 0]] = 'oops'
   hash((0, 0)) == hash((0, 0))
   sorted(grid)
   ```
4. Run it: `python3 -i < shell-why-a-tuple-can-be-a-key-and-a-list-cannot.py`.
5. Check it from the repository root: `./check m19l01-06`.

## Expected output

```text
'start'
Traceback (most recent call last):
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
True
[(0, 0), (2, 3)]
```

## How to check

`./check m19l01-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-why-a-tuple-can-be-a-key-and-a-list-cannot.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
