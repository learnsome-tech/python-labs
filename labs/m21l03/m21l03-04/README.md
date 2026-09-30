# m21l03-04 · Printing and parsing: strftime and strptime

**Lesson:** [Dates, Times And Random](https://learnsome.tech/learn/python-course/m21l03) (lesson 21.3, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can make and compare dates, do arithmetic with timedelta, format and parse them with strftime and strptime, and generate random numbers you can reproduce with a seed.

In the lesson: Two methods with unfriendly names do the conversions. The first is s t r f time, string format time, which turns a datetime into text the way you want it. You hand it a pattern of percent codes: capital Y for the four digit year, capital B for the month name, capital H and capital M for hours and minutes. Its mirror image is s t r p time, string parse time, a function on the datetime type that reads text using the same codes and gives you a real datetime. Once both sides are real values, subtracting them gives a timedelta which knows both its days and its total seconds. One more line at the end: weekday numbers the days from Monday at zero, and the iso format method gives the standard text form. Run it and read down.

## Files

- [`starter/dateFormat.py`](starter/dateFormat.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l03/m21l03-04/starter`
2. Read `dateFormat.py` the way the lesson builds it:
   - Lines 1–5: string format time
   - Lines 6–10: string parse time
   - Lines 11–13: one more line
3. Notes from the lesson:
   - Line 5: percent codes: day, month name, year, hour, minute
   - Line 7: same codes, read backwards: text in, datetime out
4. Run it: `python3 dateFormat.py`.
5. Check it from the repository root: `./check m21l03-04`.

## Expected output

```text
2026-03-14 09:30:00
14 March 2026 at 09:30
286 days, 8:30:00
286 24741000.0
2026-04-13 5 2026-03-14
```

## How to check

`./check m21l03-04` copies `starter/` into a scratch directory and runs `python3 dateFormat.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
