# m17l01-06 · The as clause hands you the object

**Lesson:** [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) (lesson 17.1, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can wrap risky work in a try statement, catch the particular exception it may raise, use the as clause, else and finally correctly, and keep a program alive through bad input.

In the lesson: An exception is an object, and it carries information. Add the word as and a name to the except clause and the object is yours inside the handler. Here we ask it three things it can tell us. Its type name, which is the word you saw before the colon in the traceback. Its message, which is what printing the object gives you: the same wording that came after the colon. And its args, the tuple of arguments the exception was created with, which for most built in exceptions holds just that message. The name err is an ordinary variable, so you can put it in a log line or in your own message to the user.

## Files

- [`starter/exceptobject.py`](starter/exceptobject.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l01/m17l01-06/starter`
2. Read `exceptobject.py`.
3. Run it: `python3 exceptobject.py`.
4. Check it from the repository root: `./check m17l01-06`.

## Expected output

```text
type is ValueError
message is invalid literal for int() with base 10: '12x'
args is ("invalid literal for int() with base 10: '12x'",)
```

## How to check

`./check m17l01-06` copies `starter/` into a scratch directory and runs `python3 exceptobject.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
