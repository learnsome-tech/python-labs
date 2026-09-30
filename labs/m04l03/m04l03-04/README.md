# m04l03-04 · Digits in quotes are still a string

**Lesson:** [Strings, Delimiters And Concatenation](https://learnsome.tech/learn/python-course/m04l03) (lesson 4.3, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write string literals with either delimiter, tell a string of digits from an integer, concatenate and repeat strings, and fix the type error that mixing the two produces.

In the lesson: Strings are a new Python type. Call the type function on the string dog, and the answer is class str, which is Python's name for the string type. Now try the digit seven in quotes. The answer is still class str. Then try the very same digit without the quotes, and the answer is class int. The last two lines show how easily you can get confused. Strings can include any characters, including digits, and quotes turn even digits into strings. What matters is the quotes, not whether the characters look numeric to you. This will have consequences in the next section.

## Files

- [`starter/shell-digits-in-quotes-are-still-a-string.py`](starter/shell-digits-in-quotes-are-still-a-string.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-04/starter`
2. Read `shell-digits-in-quotes-are-still-a-string.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   type('dog')
   type('7')
   type(7)
   ```
4. Run it: `python3 -i < shell-digits-in-quotes-are-still-a-string.py`.
5. Check it from the repository root: `./check m04l03-04`.

## Expected output

```text
<class 'str'>
<class 'str'>
<class 'int'>
```

## How to check

`./check m04l03-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-digits-in-quotes-are-still-a-string.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
