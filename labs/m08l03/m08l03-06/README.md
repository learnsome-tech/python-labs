# m08l03-06 · The string format method

**Lesson:** [Chapter One In One Sitting](https://learnsome.tech/learn/python-course/m08l03) (lesson 8.3, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can recall, in one sitting, every idea from chapter one: the types and their literals, variables, operators and precedence, strings and formatting, input and output, functions, dictionaries, loops and floats.

In the lesson: Group four, part two: the format method, the summary's example split over a few shell lines to fit the screen. Braces mark each place where a value is substituted. Leave them empty and the parameters are substituted in order; put a digit inside and it names a parameter by position, from zero. The expression inside the braces may end with a colon and a formatting string, such as dot three f, to round a number to that many places beyond the decimal point. The second form puts a key name inside the braces and passes a dictionary preceded by two stars. Both produce exactly the same string. Pass the locals function that way to use your local variables.

## Files

- [`starter/shell-the-string-format-method.py`](starter/shell-the-string-format-method.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-06/starter`
2. Read `shell-the-string-format-method.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   fmt = 'word: {}, int: {}, formatted float: {:.3f}.'
   fmt.format('Joe', 23, 2.1357)
   defs = {'name':'Joe', 'num':23, 'dec':2.13579}
   f2 = 'word: {name}, int: {num}, formatted float: {dec:.3f}.'
   f2.format(**defs)
   ```
4. Run it: `python3 -i < shell-the-string-format-method.py`.
5. Check it from the repository root: `./check m08l03-06`.

## Expected output

```text
'word: Joe, int: 23, formatted float: 2.136.'
'word: Joe, int: 23, formatted float: 2.136.'
```

## How to check

`./check m08l03-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-string-format-method.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
