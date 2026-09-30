# m09l03-08 · Predicting find on a short line

**Lesson:** [String Slices](https://learnsome.tech/learn/python-course/m09l03) (lesson 9.3, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

In the lesson: Predict each line before you test it. The first letter e is at index one, inside Hello. The lowercase substring h followed by e appears at index eight, in the word there; the capital H at the start does not match, because find is case sensitive. Starting the search at index ten steps over both and finds the letter e at index eleven. And the last line looks for the lowercase h from index ten onward, where none remains, so it returns minus one.

## Files

- [`starter/shell-predicting-find-on-a-short-line.py`](starter/shell-predicting-find-on-a-short-line.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l03/m09l03-08/starter`
2. Read `shell-predicting-find-on-a-short-line.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   #       0123456789012
   line = 'Hello, there!'
   line.find('e')
   line.find('he')
   line.find('e', 10)
   line.find('he', 10)
   ```
4. Run it: `python3 -i < shell-predicting-find-on-a-short-line.py`.
5. Check it from the repository root: `./check m09l03-08`.

## Expected output

```text
1
8
11
-1
```

## How to check

`./check m09l03-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-predicting-find-on-a-short-line.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
