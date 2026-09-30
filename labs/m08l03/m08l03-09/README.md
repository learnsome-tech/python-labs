# m08l03-09 · Dictionaries

**Lesson:** [Chapter One In One Sitting](https://learnsome.tech/learn/python-course/m08l03) (lesson 8.3, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can recall, in one sitting, every idea from chapter one: the types and their literals, variables, operators and precedence, strings and formatting, input and output, functions, dictionaries, loops and floats.

In the lesson: Group seven: dictionaries. A dictionary associates each key with a value, and the key may be any immutable type, which includes numbers and strings. Calling dict with no parameters gives you one that starts empty. To store an association, write the dictionary name, the key expression in square brackets, an equals sign, and the value expression. That same square bracket form inside a larger expression does the opposite: it gives you back the value stored under that key. Ask for the whole dictionary and the shell shows every pair; ask the len function and it tells you how many pairs there are.

## Files

- [`starter/shell-dictionaries.py`](starter/shell-dictionaries.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-09/starter`
2. Read `shell-dictionaries.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   prices = dict()
   prices['apple'] = 35
   prices['pear'] = 40
   prices
   prices['apple']
   len(prices)
   ```
4. Run it: `python3 -i < shell-dictionaries.py`.
5. Check it from the repository root: `./check m08l03-09`.

## Expected output

```text
{'apple': 35, 'pear': 40}
35
2
```

## How to check

`./check m08l03-09` copies `starter/` into a scratch directory and runs `python3 -i < shell-dictionaries.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
