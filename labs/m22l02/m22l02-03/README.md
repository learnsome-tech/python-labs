# m22l02-03 · The handful of types you actually need

**Lesson:** [Type Hints](https://learnsome.tech/learn/python-course/m22l02) (lesson 22.2, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Graded

## Goal

You can annotate a function's parameters and return value, write the common types including lists, dictionaries and optional values, explain that hints change nothing at runtime, and check them with mypy.

In the lesson: In practice a handful of types cover nearly everything. The four builtin names: int, float, str and bool. A list of something, written as list with the item type in square brackets. A dictionary, written as dict with the key type and the value type, in that order. A tuple, either with a type per position or with one type and three dots for any number of them. And the optional case, written with the vertical bar and None. Two notes on history. Before version three point nine you had to import capitalised versions of these from the typing module, which is why old code looks different. And the vertical bar arrived in three point ten. Here they are in use, with the two lines it prints.

## Files

- [`starter/typedTools.py`](starter/typedTools.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m22l02/m22l02-03/starter`
2. Read `typedTools.py`.
3. Run it: `python3 typedTools.py`.
4. Check it from the repository root: `./check m22l02-03`.

## Expected output

```text
{'hi': 2, 'there': 5}
4 None
```

## How to check

`./check m22l02-03` copies `starter/` into a scratch directory and runs `python3 typedTools.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
