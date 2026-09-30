# m21l04-06 · re: patterns, in one careful segment

**Lesson:** [A Standard Library Tour](https://learnsome.tech/learn/python-course/m21l04) (lesson 21.4, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can name the standard library modules a beginner actually meets, say what each one is for, recognise when a problem belongs to one of them, and look the details up for yourself.

In the lesson: Last, and most feared, the r e module: regular expressions, a tiny language for describing patterns in text. Four functions carry most of the load. Find all returns every match as a list. Search finds the first one and gives you a match object, whose groups are the bracketed pieces of the pattern. Sub replaces every match. And compile turns a pattern you use often into an object with the same methods. Two habits to form now. Write the pattern as a raw string, with an r in front of it, so Python leaves the backslashes alone for the pattern language. And remember that a failed match returns None, which is the last line of output here, and using it without checking is the classic regular expression crash.

## Files

- [`starter/regexDemo.py`](starter/regexDemo.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l04/m21l04-06/starter`
2. Read `regexDemo.py`.
3. Notes from the lesson:
   - Line 5: the r prefix stops Python eating the backslashes
   - Line 15: no match returns None, so always check before using it
4. Run it: `python3 regexDemo.py`.
5. Check it from the repository root: `./check m21l04-06`.

## Expected output

```text
['1234', '2026', '03', '14']
2026-03-14 2026
Order XXXX shipped on XXXX-XX-XX to Ada
1234
None
```

## How to check

`./check m21l04-06` copies `starter/` into a scratch directory and runs `python3 regexDemo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
