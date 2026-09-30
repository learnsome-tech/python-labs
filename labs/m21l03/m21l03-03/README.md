# m21l03-03 · Building dates and doing arithmetic

**Lesson:** [Dates, Times And Random](https://learnsome.tech/learn/python-course/m21l03) (lesson 21.3, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can make and compare dates, do arithmetic with timedelta, format and parse them with strftime and strptime, and generate random numbers you can reproduce with a seed.

In the lesson: Import the two names and build a date by hand. You pass the year, month and day, in that big to small order, and Python checks them, so an impossible day is an error rather than a bug you find in June. Asked plainly, the shell shows the constructor call that would rebuild it. Print it and you get the international standard layout instead, year then month then day. Now the useful part. Add a timedelta of forty five days and it lands in March, and nobody had to remember how long January is. Subtract two dates and you get a timedelta back. Ask it for days and you have your answer as a plain number, ready for arithmetic.

## Files

- [`starter/shell-building-dates-and-doing-arithmetic.py`](starter/shell-building-dates-and-doing-arithmetic.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l03/m21l03-03/starter`
2. Read `shell-building-dates-and-doing-arithmetic.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   from datetime import date, timedelta
   payday = date(2026, 1, 30)
   payday
   print(payday)
   payday + timedelta(days=45)
   date(2026, 3, 16) - payday
   (date(2026, 3, 16) - payday).days
   ```
4. Run it: `python3 -i < shell-building-dates-and-doing-arithmetic.py`.
5. Check it from the repository root: `./check m21l03-03`.

## Expected output

```text
datetime.date(2026, 1, 30)
2026-01-30
datetime.date(2026, 3, 16)
datetime.timedelta(days=45)
45
```

## How to check

`./check m21l03-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-building-dates-and-doing-arithmetic.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
