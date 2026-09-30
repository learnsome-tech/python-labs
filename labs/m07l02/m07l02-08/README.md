# m07l02-08 · arithDict.py formats with locals

**Lesson:** [Dictionaries And String Formatting](https://learnsome.tech/learn/python-course/m07l02) (lesson 7.2, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can build strings with the format method and a dictionary unpacked by two stars, and use locals or an f-string to drop local variable values straight into a format string.

In the lesson: Run the example program arithDict. Four ordinary variables are set up: x, y, their sum and their product. Note the variable names inside braces in formatStr, and note the dictionary reference used as the format parameter, two stars followed by locals. A string like formatStr is probably the most readable way to code the creation of a string from a collection of literal strings and program values. The ending part of the syntax may appear a bit strange at first, but it is very useful. It clearly indicates how values are embedded into the format string, and it avoids having a long list of parameters to format. The result is one tidy line of arithmetic.

## Files

- [`starter/arithDict.py`](starter/arithDict.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l02/m07l02-08/starter`
2. Read `arithDict.py` the way the lesson builds it:
   - Lines 1–6: Four ordinary variables
   - Lines 7: the variable names inside braces
   - Lines 8–9: one tidy line
3. Notes from the lesson:
   - Line 8: **locals() supplies one keyword argument per local variable
4. Run it: `python3 arithDict.py`.
5. Check it from the repository root: `./check m07l02-08`.

## Expected output

```text
20 + 30 = 50; 20 * 30 = 600.
```

## How to check

`./check m07l02-08` copies `starter/` into a scratch directory and runs `python3 arithDict.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
