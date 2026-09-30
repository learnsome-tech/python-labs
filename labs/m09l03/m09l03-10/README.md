# m09l03-10 · Lists index and slice the same way

**Lesson:** [String Slices](https://learnsome.tech/learn/python-course/m09l03) (lesson 9.3, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

In the lesson: Indexing and slicing work on any kind of Python sequence, so you can index or slice lists too. Read this shell session. Index one gives the second element, the number seven, counting from zero exactly as with characters. Minus two gives the second element from the right end, the number six. And the slice from one to four gives a new list of three elements. Slicing a list gives a list, while slicing a string gives a string. Unlike strings, lists are mutable, as you will see when we come to appending.

## Files

- [`starter/shell-lists-index-and-slice-the-same-way.py`](starter/shell-lists-index-and-slice-the-same-way.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l03/m09l03-10/starter`
2. Read `shell-lists-index-and-slice-the-same-way.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   vals = [5, 7, 9, 22, 6, 8]
   vals[1]
   vals[-2]
   vals[1:4]
   ```
4. Run it: `python3 -i < shell-lists-index-and-slice-the-same-way.py`.
5. Check it from the repository root: `./check m09l03-10`.

## Expected output

```text
7
6
[7, 9, 22]
```

## How to check

`./check m09l03-10` copies `starter/` into a scratch directory and runs `python3 -i < shell-lists-index-and-slice-the-same-way.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
