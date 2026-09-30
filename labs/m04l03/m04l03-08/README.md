# m04l03-08 · Mixed types, and the two ways to fix it

**Lesson:** [Strings, Delimiters And Concatenation](https://learnsome.tech/learn/python-course/m04l03) (lesson 4.3, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write string literals with either delimiter, tell a string of digits from an integer, concatenate and repeat strings, and fix the type error that mixing the two produces.

In the lesson: Now the third line, with one in quotes and one not. With mixed string and int types, Python sees an ambiguous expression, and does not guess which you want. It just gives an error. Be careful if you are a Java or C sharp programmer. That is unlike those languages, where the integer would be automatically converted to the string two, so the concatenation would make sense. You need to make an explicit conversion. Make them both strings, using the str function on the integer, if you mean concatenation, and you get the two character string. Or make them both integers, using the int function on the string, if you mean addition, and you get nine. With literal values these are only illustrations. With variables, starting in the next module, expressions involving these conversions become far more important.

## Files

- [`starter/shell-mixed-types-and-the-two-ways-to-fix-it.py`](starter/shell-mixed-types-and-the-two-ways-to-fix-it.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-08/starter`
2. Read `shell-mixed-types-and-the-two-ways-to-fix-it.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   '7'+2
   '7' + str(2)
   int('7') + 2
   ```
4. Run it: `python3 -i < shell-mixed-types-and-the-two-ways-to-fix-it.py`.
5. Check it from the repository root: `./check m04l03-08`.

## Expected output

```text
Traceback (most recent call last):
TypeError: can only concatenate str (not "int") to str
'72'
9
```

## How to check

`./check m04l03-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-mixed-types-and-the-two-ways-to-fix-it.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
