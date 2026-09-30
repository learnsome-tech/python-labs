# m03l03-03 · Asking what type a value has

**Lesson:** [Types And Functions, A Whirlwind Tour](https://learnsome.tech/learn/python-course/m03l03) (lesson 3.3, module 3: Meet Idle And The Shell) · Pro  
**Check:** Graded

## Goal

You can name four kinds of Python data, call a function with none, one or several parameters, ask type and len about a value, convert between numbers and strings, and re-enter an earlier shell line in Idle.

In the lesson: One function is called type, and it returns the type of any object. The Python Shell will evaluate functions for you. At the triple angle bracket prompt, enter type of seven, and always remember to end with the Return or Enter key. In the result, int is the way Python abbreviates integer, and the word class is basically a synonym for type in Python. Note again that the line with the value produced by the shell does not start with the prompt and appears at the left margin. For the rest of this module, enter each line individually at the prompt. The name in the second result is float, not real and not decimal, and it comes from the term floating point, for reasons explained later when we look at numbers in depth. In the third result you see another abbreviation, str rather than string. And the fourth says list.

## Files

- [`starter/shell-asking-what-type-a-value-has.py`](starter/shell-asking-what-type-a-value-has.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-03/starter`
2. Read `shell-asking-what-type-a-value-has.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   type(7)
   type(1.25)
   type('hello')
   type([1, 2, 3])
   ```
4. Run it: `python3 -i < shell-asking-what-type-a-value-has.py`.
5. Check it from the repository root: `./check m03l03-03`.

## Expected output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
```

## How to check

`./check m03l03-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-asking-what-type-a-value-has.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
