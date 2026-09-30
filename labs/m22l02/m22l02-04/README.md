# m22l02-04 · Nothing checks them while the program runs

**Lesson:** [Type Hints](https://learnsome.tech/learn/python-course/m22l02) (lesson 22.2, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Graded

## Goal

You can annotate a function's parameters and return value, write the common types including lists, dictionaries and optional values, explain that hints change nothing at runtime, and check them with mypy.

In the lesson: This is the point people most often get wrong, so watch it happen. The function promises to take an integer. Pass it a string instead and look at the second line of output: it doubles the string, because multiplying a string by two is perfectly legal in Python, and Python does not care what the annotation said. There is no error, no warning, nothing. The hints are not lies exactly, but they are unenforced. What Python does do is keep them: they are stored on the function in a dictionary of annotations, which is what makes them useful. Your editor reads that. A checker reads that. The language itself never looks at it once the file has loaded.

## Files

- [`starter/double.py`](starter/double.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m22l02/m22l02-04/starter`
2. Read `double.py`.
3. Notes from the lesson:
   - Line 6: a string where an int was promised: Python does not care
   - Line 7: the hints are stored, and any tool can read them
4. Run it: `python3 double.py`.
5. Check it from the repository root: `./check m22l02-04`.

## Expected output

```text
42
abab
{'n': <class 'int'>, 'return': <class 'int'>}
```

## How to check

`./check m22l02-04` copies `starter/` into a scratch directory and runs `python3 double.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
