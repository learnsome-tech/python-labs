# m09l02-06 · A shorter string, and the classic off by one

**Lesson:** [String Indices](https://learnsome.tech/learn/python-course/m09l02) (lesson 9.2, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can pick any character out of a string by index, count either from the front starting at zero or from the right end starting at minus one, and say why an index equal to the length raises IndexError.

In the lesson: Continue with a shorter string so the arithmetic is easy to check in your head. The word horse has length five, so its valid forward indices are zero through four, and its backward indices are minus five through minus one. Minus one gives the letter e, the last one, as it always does. Then the last line is the trap. Index one is not the first character; it is the second, the letter o. Be careful, and remember what the initial index is. Almost every off by one mistake a beginner makes comes from reading index one as the first thing rather than the second.

## Files

- [`starter/shell-a-shorter-string-and-the-classic-off-by-one.py`](starter/shell-a-shorter-string-and-the-classic-off-by-one.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l02/m09l02-06/starter`
2. Read `shell-a-shorter-string-and-the-classic-off-by-one.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   it = 'horse'
   len(it)
   it[-1]
   it[1]
   ```
4. Run it: `python3 -i < shell-a-shorter-string-and-the-classic-off-by-one.py`.
5. Check it from the repository root: `./check m09l02-06`.

## Expected output

```text
5
'e'
'o'
```

## How to check

`./check m09l02-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-a-shorter-string-and-the-classic-off-by-one.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
