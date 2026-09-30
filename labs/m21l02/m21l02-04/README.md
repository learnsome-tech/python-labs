# m21l02-04 · Straight to a file, and straight back

**Lesson:** [JSON And CSV](https://learnsome.tech/learn/python-course/m21l02) (lesson 21.2, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can save and load Python data as JSON, say which Python types survive the trip, and read a comma separated file with the csv module instead of splitting the line yourself.

In the lesson: Most of the time you want a file rather than a string, and that is dump without the s, and load without the s. Dump takes the data first and the open file second, and writes straight into it. The indent argument is worth knowing: with it the file is laid out one key per line for a human to read, and without it everything lands on one long line, which is smaller and fine for a machine. Then load without the s reads an open file and gives the data back. Here is the file it wrote, printed as text, and then the dictionary that came back out of it, still a dictionary with real numbers inside. Four functions, and you can save any data you can build.

## Files

- [`starter/jsonFile.py`](starter/jsonFile.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l02/m21l02-04/starter`
2. Read `jsonFile.py` the way the lesson builds it:
   - Lines 1–6: dump without the s
   - Lines 7–13: load without the s
3. Notes from the lesson:
   - Line 6: the data first, then the open file to write it into
   - Line 6: indent makes it readable; leave it out and it is one long line
4. Run it: `python3 jsonFile.py`.
5. Check it from the repository root: `./check m21l02-04`.

## Expected output

```text
{
  "ada": 91,
  "grace": 88,
  "alan": 95
}
88 <class 'dict'>
```

## How to check

`./check m21l02-04` copies `starter/` into a scratch directory and runs `python3 jsonFile.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
