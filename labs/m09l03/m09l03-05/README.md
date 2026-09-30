# m09l03-05 · Slices are forgiving about the end

**Lesson:** [String Slices](https://learnsome.tech/learn/python-course/m09l03) (lesson 9.3, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

In the lesson: Python evaluates slices in a more forgiving manner than it does single character indexing. In a slice, if you give an index past the limit of where it could possibly be, Python assumes you mean the actual end. So asking for everything up to index nine of a seven character string gives the whole string, with no error. Asking for the slice from eight to ten, entirely beyond the end, gives the empty string, where a single index raised an IndexError for that same number. The last line is a reminder that a slice is a string like any other, so len works on it.

## Files

- [`starter/shell-slices-are-forgiving-about-the-end.py`](starter/shell-slices-are-forgiving-about-the-end.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l03/m09l03-05/starter`
2. Read `shell-slices-are-forgiving-about-the-end.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   word = 'program'
   word[:9]
   word[8:10]
   len(word[2:5])
   ```
4. Run it: `python3 -i < shell-slices-are-forgiving-about-the-end.py`.
5. Check it from the repository root: `./check m09l03-05`.

## Expected output

```text
'program'
''
3
```

## How to check

`./check m09l03-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-slices-are-forgiving-about-the-end.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
