# m17l03-04 · When the bottom frame is not your code

**Lesson:** [Reading A Traceback Like A Professional](https://learnsome.tech/learn/python-course/m17l03) (lesson 17.3, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can read a multi-frame traceback bottom up, tell your own frames from a library's, recognise the errors that arrive before execution starts, and name the likely cause behind each of the common exception types.

In the lesson: Now a traceback that goes somewhere else. This program asks the statistics module for a mean, and asks it for the mean of an empty list. The bottom frame is a file you have never opened, deep inside the standard library, and I have shortened its path to fit the screen. Do not be alarmed by it. The library did not break; it raised on purpose, and the message tells you the rule you broke: a mean needs at least one data point. Notice too that the type name has the module in front of it, because that exception is defined in the statistics module rather than being built in.

## Files

- [`starter/meanscores.py`](starter/meanscores.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l03/m17l03-04/starter`
2. Read `meanscores.py`.
3. Run it: `python3 meanscores.py`.
4. Check it from the repository root: `./check m17l03-04`.

## Expected output

```text
average is 7
Traceback (most recent call last):
  File "meanscores.py", line 10, in <module>
    report([])
    ~~~~~~^^^^
  File "meanscores.py", line 7, in report
    print('average is', average(scores))
                        ~~~~~~~^^^^^^^^
  File "meanscores.py", line 4, in average
    return statistics.mean(scores)
           ~~~~~~~~~~~~~~~^^^^^^^^
  File ".../python3.14/statistics.py", line 177, in mean
    raise StatisticsError('mean requires at least one data point')
statistics.StatisticsError: mean requires at least one data point
```

## How to check

`./check m17l03-04` copies `starter/` into a scratch directory and runs `python3 meanscores.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
