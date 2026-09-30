# m17l02-05 · Re-raising: handle a little, then get out of the way

**Lesson:** [Raising, And Writing Your Own Exception](https://learnsome.tech/learn/python-course/m17l02) (lesson 17.2, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can raise a built-in exception with a useful message to refuse bad input, re-raise after logging, chain one exception to another, and define a small exception class of your own when the situation calls for it.

In the lesson: Sometimes you want to notice an exception without claiming to have dealt with it. Here the function writes a line to a log and then, on the last line of the handler, uses the word raise on its own, with nothing after it. Inside an except block that means: send the very same exception on its way again. Run it, and the log line appears, and then the traceback arrives at the top of the program as if we had never interfered. Two details are worth your attention. The traceback still points at the int call on the third line, the real origin, not at our raise. And this is the honest way to log, because a handler that logs and swallows leaves the caller believing all was well.

## Files

- [`starter/relog.py`](starter/relog.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l02/m17l02-05/starter`
2. Read `relog.py`.
3. Notes from the lesson:
   - Line 6: raise on its own re-raises the exception being handled
4. Run it: `python3 relog.py`.
5. Check it from the repository root: `./check m17l02-05`.

## Expected output

```text
12
log: bad count from the user: 'a few'
Traceback (most recent call last):
  File "relog.py", line 9, in <module>
    print(parse_count('a few'))
          ~~~~~~~~~~~^^^^^^^^^
  File "relog.py", line 3, in parse_count
    return int(text)
ValueError: invalid literal for int() with base 10: 'a few'
```

## How to check

`./check m17l02-05` copies `starter/` into a scratch directory and runs `python3 relog.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
