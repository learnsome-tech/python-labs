# m21l03-02 · What time is it now?

**Lesson:** [Dates, Times And Random](https://learnsome.tech/learn/python-course/m21l03) (lesson 21.3, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can make and compare dates, do arithmetic with timedelta, format and parse them with strftime and strptime, and generate random numbers you can reproduce with a seed.

In the lesson: The clock is where most programs start. The now function of the datetime type reads your computer's clock and hands you a datetime. I cannot print it here, because the answer would be different by the time you watch this, so we ask questions about it instead. Its type is datetime. Its year is at least twenty twenty six. Its hour lies between zero and twenty three and its month between one and twelve, since every part is available as an attribute. And the date method gives you the day part alone, throwing away the time. That is worth remembering the first time you compare a timestamp with a birthday and find they are never equal.

## Files

- [`starter/whenNow.py`](starter/whenNow.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l03/m21l03-02/starter`
2. Read `whenNow.py`.
3. Run it: `python3 whenNow.py`.
4. Check it from the repository root: `./check m21l03-02`.

## Expected output

```text
<class 'datetime.datetime'>
True
True True
10 True
```

## How to check

`./check m21l03-02` copies `starter/` into a scratch directory and runs `python3 whenNow.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
