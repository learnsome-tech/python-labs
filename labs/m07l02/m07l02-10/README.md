# m07l02-10 · F-strings: the same thing, shorter

**Lesson:** [Dictionaries And String Formatting](https://learnsome.tech/learn/python-course/m07l02) (lesson 7.2, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can build strings with the format method and a dictionary unpacked by two stars, and use locals or an f-string to drop local variable values straight into a format string.

In the lesson: One more, and this one is optional but handy. A simplification for formatting was added in Python three point six: the f string. It has many features, but the simplest thing it does is to shorten the formatting of a literal string that refers to local variables, like the one we just saw. Merely add the letter f immediately before the literal format string, and eliminate the call to the format method with locals. The example is arithfstring, and it prints exactly the same line as arithDict did. The two comments at the end of the file make the point: the f goes directly before the literal format string, and local variable values are substituted automatically.

## Files

- [`starter/arithfstring.py`](starter/arithfstring.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l02/m07l02-10/starter`
2. Read `arithfstring.py`.
3. Run it: `python3 arithfstring.py`.
4. Check it from the repository root: `./check m07l02-10`.

## Expected output

```text
20 + 30 = 50; 20 * 30 = 600.
```

## How to check

`./check m07l02-10` copies `starter/` into a scratch directory and runs `python3 arithfstring.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
