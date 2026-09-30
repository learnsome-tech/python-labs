# m09l03-02 · The first slices

**Lesson:** [String Slices](https://learnsome.tech/learn/python-course/m09l03) (lesson 9.3, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

In the lesson: Try the first slice expression, and read it aloud as: start at index zero, stop before index four. You get the first four characters, and the letter u at index four is the first one past the slice, not included. Now predict and try the next two lines. Start at two and stop before five gives three characters, at indices two, three and four. Start at one and stop before three gives two. Subtract the first number from the second and you know how many characters to expect.

## Files

- [`starter/shell-the-first-slices.py`](starter/shell-the-first-slices.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l03/m09l03-02/starter`
2. Read `shell-the-first-slices.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   s = 'computer'
   s[0:4]
   s[2:5]
   s[1:3]
   ```
4. Run it: `python3 -i < shell-the-first-slices.py`.
5. Check it from the repository root: `./check m09l03-02`.

## Expected output

```text
'comp'
'mpu'
'om'
```

## How to check

`./check m09l03-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-first-slices.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
