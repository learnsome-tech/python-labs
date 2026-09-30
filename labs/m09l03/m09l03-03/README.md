# m09l03-03 · Leaving a bound out

**Lesson:** [String Slices](https://learnsome.tech/learn/python-course/m09l03) (lesson 9.3, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

In the lesson: If you omit the first index, the slice starts from the beginning. If you omit the second index, the slice goes all the way to the end. Predict and try each line individually. Nothing before the colon means start at zero, so the first line gives the first three characters. Nothing after the colon means run to the end, so the second gives everything from index five onward. And if you omit both, you get the whole string back, which sounds pointless until you meet lists, where the same expression copies one.

## Files

- [`starter/shell-leaving-a-bound-out.py`](starter/shell-leaving-a-bound-out.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l03/m09l03-03/starter`
2. Read `shell-leaving-a-bound-out.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   s = 'computer'
   s[:3]
   s[5:]
   s[:]
   ```
4. Run it: `python3 -i < shell-leaving-a-bound-out.py`.
5. Check it from the repository root: `./check m09l03-03`.

## Expected output

```text
'com'
'ter'
'computer'
```

## How to check

`./check m09l03-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-leaving-a-bound-out.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
