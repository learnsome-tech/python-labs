# m09l02-05 · Predicting the negative indices

**Lesson:** [String Indices](https://learnsome.tech/learn/python-course/m09l02) (lesson 9.2, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can pick any character out of a string by index, count either from the front starting at zero or from the right end starting at minus one, and say why an index equal to the length raises IndexError.

In the lesson: Predict each line before you run it, then test it one line at a time. Minus one is the last character, the letter r. Minus three counts back three places from the right end and lands on the letter t. And minus ten walks off the left-hand end of an eight character string, so it is out of range in just the same way index eight was, and you get the same IndexError. The forgiving behaviour you may have heard about belongs to slices, which are the subject of the next module, not to single characters. Ask for a character that is not there, from either end, and Python raises an error rather than guessing what you meant.

## Files

- [`starter/shell-predicting-the-negative-indices.py`](starter/shell-predicting-the-negative-indices.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l02/m09l02-05/starter`
2. Read `shell-predicting-the-negative-indices.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   s = 'computer'
   s[-1]
   s[-3]
   s[-10]
   ```
4. Run it: `python3 -i < shell-predicting-the-negative-indices.py`.
5. Check it from the repository root: `./check m09l02-05`.

## Expected output

```text
'r'
't'
Traceback (most recent call last):
IndexError: string index out of range
```

## How to check

`./check m09l02-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-predicting-the-negative-indices.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
