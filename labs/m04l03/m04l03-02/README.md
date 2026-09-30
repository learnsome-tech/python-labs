# m04l03-02 · Either delimiter will do

**Lesson:** [Strings, Delimiters And Concatenation](https://learnsome.tech/learn/python-course/m04l03) (lesson 4.3, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write string literals with either delimiter, tell a string of digits from an integer, concatenate and repeat strings, and fix the type error that mixing the two produces.

In the lesson: Type the word hello enclosed in double quotes. Python gives the string back to you, but note that the interpreter gives it back with single quotes. Python does not care what system you use when you type it in. When it displays a string for you, it prefers the single quote, unless the string itself contains one, so do not be surprised when what comes back is punctuated differently from what you typed. Now enter the greeting Hi with an exclamation mark, this time in single quotes. That works just as well. Having the choice of delimiters can be handy, and the next screen shows exactly when.

## Files

- [`starter/shell-either-delimiter-will-do.py`](starter/shell-either-delimiter-will-do.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-02/starter`
2. Read `shell-either-delimiter-will-do.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   "hello"
   'Hi!'
   ```
4. Run it: `python3 -i < shell-either-delimiter-will-do.py`.
5. Check it from the repository root: `./check m04l03-02`.

## Expected output

```text
'hello'
'Hi!'
```

## How to check

`./check m04l03-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-either-delimiter-will-do.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
