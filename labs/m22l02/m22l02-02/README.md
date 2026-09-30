# m22l02-02 · Annotating parameters and the return

**Lesson:** [Type Hints](https://learnsome.tech/learn/python-course/m22l02) (lesson 22.2, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Graded

## Goal

You can annotate a function's parameters and return value, write the common types including lists, dictionaries and optional values, explain that hints change nothing at runtime, and check them with mypy.

In the lesson: The syntax is small. After a parameter name write a colon and the type. After the closing bracket write an arrow, made of a hyphen and a greater than sign, and the type that comes back. A parameter with a default gets both, with the default after the type. The second function shows the single most useful hint of all: str, then a vertical bar, then None. The vertical bar means one type or the other, and this says the function returns a string when it finds the user and None when it does not, which is exactly the case people forget to handle. The program runs exactly as it would without a single annotation, and prints the same three lines.

## Files

- [`starter/cart.py`](starter/cart.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m22l02/m22l02-02/starter`
2. Read `cart.py` the way the lesson builds it:
   - Lines 1–2: a colon and the type
   - Lines 3–7: the second function
   - Lines 8–12: The program runs exactly as it would
3. Notes from the lesson:
   - Line 1: each parameter, then the arrow and the returned type
   - Line 5: str or None: the vertical bar means one type or the other
4. Run it: `python3 cart.py`.
5. Check it from the repository root: `./check m22l02-02`.

## Expected output

```text
5.5
2.75
ada@example.com None
```

## How to check

`./check m22l02-02` copies `starter/` into a scratch directory and runs `python3 cart.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
