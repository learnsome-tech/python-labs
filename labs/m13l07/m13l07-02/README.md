# m13l07-02 · Indexing works, assignment does not

**Lesson:** [Loops And Tuples](https://learnsome.tech/learn/python-course/m13l07) (lesson 13.7, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can package related values in a tuple, unpack a tuple in a for loop heading, and replace a long repetitive if elif statement with a loop over a list of tuples.

In the lesson: Let us test those claims in the shell. Type a tuple literal and the shell echoes it back inside parentheses, though as the chapter summary will show, it is really the comma that makes a tuple and the parentheses only group. Give the pair of strings a name, and indexing works exactly as it does for a list: index zero is the first part, and the length function counts the parts. Now try to assign to an element. Python refuses, with a type error saying a tuple object does not support item assignment. That refusal is the point of a tuple: it is a fixed grouping, settled when it is built.

## Files

- [`starter/shell-indexing-works-assignment-does-not.py`](starter/shell-indexing-works-assignment-does-not.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l07/m13l07-02/starter`
2. Read `shell-indexing-works-assignment-does-not.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   (1, 2, 3)
   ('yes', 'no')
   pair = ('yes', 'no')
   pair[0]
   len(pair)
   pair[0] = 'maybe'
   ```
4. Run it: `python3 -i < shell-indexing-works-assignment-does-not.py`.
5. Check it from the repository root: `./check m13l07-02`.

## Expected output

```text
(1, 2, 3)
('yes', 'no')
'yes'
2
Traceback (most recent call last):
TypeError: 'tuple' object does not support item assignment
```

## How to check

`./check m13l07-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-indexing-works-assignment-does-not.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
