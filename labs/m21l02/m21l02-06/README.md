# m21l02-06 · DictReader, and why you do not split yourself

**Lesson:** [JSON And CSV](https://learnsome.tech/learn/python-course/m21l02) (lesson 21.2, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can save and load Python data as JSON, say which Python types survive the trip, and read a comma separated file with the csv module instead of splitting the line yourself.

In the lesson: Dict reader is the one to reach for. It treats the first line as the header row and gives you a dictionary per row, so you ask for a column by name rather than counting positions. That means inserting a column into the file cannot silently break your program, which counting positions absolutely does. Here the visits column is converted to an integer and doubled, because remember, everything arrives as text. Then the last two lines make the case for the module. Take that same row and split it on a comma yourself, and the city tears in half: two broken fields with stray quote marks. The rules for quoting, embedded commas, doubled quotes and newlines inside fields are real, and the module already implements all of them.

## Files

- [`starter/csvDict.py`](starter/csvDict.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l02/m21l02-06/starter`
2. Read `csvDict.py`.
3. Run it: `python3 csvDict.py`.
4. Check it from the repository root: `./check m21l02-06`.

## Expected output

```text
Ada London 6
Grace New York, NY 14
['Grace', '"New York', ' NY"', '7']
```

## How to check

`./check m21l02-06` copies `starter/` into a scratch directory and runs `python3 csvDict.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
