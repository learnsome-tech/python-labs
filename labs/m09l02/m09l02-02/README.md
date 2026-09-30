# m09l02-02 · Indexing computer, and one index too far

**Lesson:** [String Indices](https://learnsome.tech/learn/python-course/m09l02) (lesson 9.2, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can pick any character out of a string by index, count either from the front starting at zero or from the right end starting at minus one, and say why an index equal to the length raises IndexError.

In the lesson: Enter these one at a time in the shell. You can skip the comment; it is there only to make the indices explicit above the letters. Index zero gives the first character, the letter c. Index five gives the letter t, and you can check that against the table. Now try index eight. You cannot refer directly to a character that is not there, and Python says so with an IndexError: string index out of range. The indices only go up to seven in this example. Recall the len function, which gives the length of a sequence; it works on strings too. Guess the answer before you look. The length is eight, which is precisely the index that just failed.

## Files

- [`starter/shell-indexing-computer-and-one-index-too-far.py`](starter/shell-indexing-computer-and-one-index-too-far.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l02/m09l02-02/starter`
2. Read `shell-indexing-computer-and-one-index-too-far.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   #    01234567
   s = 'computer'
   s[0]
   s[5]
   s[8]
   len(s)
   ```
4. Run it: `python3 -i < shell-indexing-computer-and-one-index-too-far.py`.
5. Check it from the repository root: `./check m09l02-02`.

## Expected output

```text
'c'
't'
Traceback (most recent call last):
IndexError: string index out of range
8
```

## How to check

`./check m09l02-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-indexing-computer-and-one-index-too-far.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
