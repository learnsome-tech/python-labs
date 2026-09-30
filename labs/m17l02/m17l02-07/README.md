# m17l02-07 · Your own exception class, in two lines

**Lesson:** [Raising, And Writing Your Own Exception](https://learnsome.tech/learn/python-course/m17l02) (lesson 17.2, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can raise a built-in exception with a useful message to refuse bad input, re-raise after logging, chain one exception to another, and define a small exception class of your own when the situation calls for it.

In the lesson: When no built in exception fits, you can make one. Here is the whole definition: the word class, your name, the word Exception in parentheses, and a body of pass. It inherits everything and adds nothing, which is what you want almost every time. Classes are properly taught three modules from here, so for today treat those two lines as a recipe. Once defined, you raise it exactly as you raised a ValueError, and you catch it in an except clause by name. Run the good swim and the cold one. Because our class is built on Exception, an except clause naming Exception would also catch it, and so would code that knows nothing about swimming.

## Files

- [`starter/toocold.py`](starter/toocold.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l02/m17l02-07/starter`
2. Read `toocold.py` the way the lesson builds it:
   - Lines 1–2: the whole definition
   - Lines 3–7: raise it exactly as you raised a ValueError
   - Lines 8–13: the good swim and the cold one
3. Notes from the lesson:
   - Line 1: class Name(Exception): inherit everything, add nothing
4. Run it: `python3 toocold.py`.
5. Check it from the repository root: `./check m17l02-07`.

## Expected output

```text
swimming in 18 degrees
caught a TooColdError: -2 degrees is too cold
```

## How to check

`./check m17l02-07` copies `starter/` into a scratch directory and runs `python3 toocold.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
