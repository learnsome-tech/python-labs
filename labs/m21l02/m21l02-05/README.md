# m21l02-05 · Rows and columns: writing and reading CSV

**Lesson:** [JSON And CSV](https://learnsome.tech/learn/python-course/m21l02) (lesson 21.2, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can save and load Python data as JSON, say which Python types survive the trip, and read a comma separated file with the csv module instead of splitting the line yourself.

In the lesson: C s v is the flat cousin: one row per line, one comma between fields, and a first row of column names. The csv module writes it and reads it. Look at the file first. The writer put quotes around New York comma N Y, because that field contains a comma and would otherwise look like two fields. Nobody had to decide that; the module knows the rules. Reading it back, csv reader hands you a list of strings for each row, and the quoted field arrives as one item with its comma intact. Notice everything is a string, including the visit counts, so convert them yourself. One detail to copy without much thought: the new line argument set to the empty string, which keeps line endings correct on every platform.

## Files

- [`starter/csvRead.py`](starter/csvRead.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l02/m21l02-05/starter`
2. Read `csvRead.py`.
3. Notes from the lesson:
   - Line 7: new line set to the empty string: the csv module handles endings
   - Line 13: each row arrives as a list of strings, always strings
4. Run it: `python3 csvRead.py`.
5. Check it from the repository root: `./check m21l02-05`.

## Expected output

```text
name,city,visits
Ada,London,3
Grace,"New York, NY",7
['name', 'city', 'visits']
['Ada', 'London', '3']
['Grace', 'New York, NY', '7']
```

## How to check

`./check m21l02-05` copies `starter/` into a scratch directory and runs `python3 csvRead.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
