# m20l02-07 · A property: behaviour behind a plain name

**Lesson:** [Methods, Attributes And self](https://learnsome.tech/learn/python-course/m20l02) (lesson 20.2, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write methods that use self, tell instance attributes from class attributes, avoid the shared mutable class attribute trap, document a method, and expose a computed value as a property.

In the lesson: Sometimes a value should look like an attribute but be worked out on demand. Here only the radius is stored; the area is derived from it. Above the method sits a decorator called property, an at sign and the word property on a line of its own. Now you read it with no parentheses, as though it were plain data, and Python quietly runs the method body each time. Change the radius, and the next read of area is already correct, so the two can never fall out of step. Because we defined only the reading half, assigning to area refuses the assignment and says there is no setter. That is the point of a property: you can start with a plain attribute and later put behaviour behind the same name, without touching a single line of code that uses it.

## Files

- [`starter/circleArea.py`](starter/circleArea.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l02/m20l02-07/starter`
2. Read `circleArea.py` the way the lesson builds it:
   - Lines 1–5: only the radius is stored
   - Lines 6–10: a decorator called property
   - Lines 11–19: refuses the assignment
3. Notes from the lesson:
   - Line 7: @property turns the method into a read-only attribute
   - Line 13: no parentheses: the method body runs on every read
   - Line 17: read-only, unless you also define a matching setter
4. Run it: `python3 circleArea.py`.
5. Check it from the repository root: `./check m20l02-07`.

## Expected output

```text
12.56636
28.27431
AttributeError: property 'area' of 'Circle' object has no setter
```

## How to check

`./check m20l02-07` copies `starter/` into a scratch directory and runs `python3 circleArea.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
