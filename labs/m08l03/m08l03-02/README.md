# m08l03-02 · Types and their literals

**Lesson:** [Chapter One In One Sitting](https://learnsome.tech/learn/python-course/m08l03) (lesson 8.3, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can recall, in one sitting, every idea from chapter one: the types and their literals, variables, operators and precedence, strings and formatting, input and output, functions, dictionaries, loops and floats.

In the lesson: Group one: the types, and how you write a literal of each. An int literal has no decimal point, and integers are stored exactly and may be arbitrarily large. A float literal must contain a decimal point, precisely so you can tell it from an int, and it approximates a wide range of values. A string literal is a sequence of characters inside matching quotes. A list literal is a comma separated collection inside square brackets, with many, one, or no elements. Calling dict gives an empty dictionary. And None is a literal with a type of its own, marking the absence of an object.

## Files

- [`starter/shell-types-and-their-literals.py`](starter/shell-types-and-their-literals.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-02/starter`
2. Read `shell-types-and-their-literals.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   type(42)
   type(4.0)
   type('hi')
   type([1, 2, 3])
   type(dict())
   type(None)
   ```
4. Run it: `python3 -i < shell-types-and-their-literals.py`.
5. Check it from the repository root: `./check m08l03-02`.

## Expected output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'NoneType'>
```

## How to check

`./check m08l03-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-types-and-their-literals.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
