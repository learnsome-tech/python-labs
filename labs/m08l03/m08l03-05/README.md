# m08l03-05 · Strings: quotes, joining, repeating

**Lesson:** [Chapter One In One Sitting](https://learnsome.tech/learn/python-course/m08l03) (lesson 8.3, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can recall, in one sitting, every idea from chapter one: the types and their literals, variables, operators and precedence, strings and formatting, input and output, functions, dictionaries, loops and floats.

In the lesson: Group four, part one: strings. A literal is characters inside matching quotes, single or double, on one line; triple quotes let a literal run across several lines of the source. Inside a literal, escape codes start with a backslash: one for a single quote, one for a newline. The binary operations keep the precedence they have in arithmetic. Plus between two strings is concatenation, running them together. A string times an integer, either way round, repeats the string that many times. The len function tells you how many characters a sequence holds. Notice that a newline inside one literal produces two lines of output.

## Files

- [`starter/shell-strings-quotes-joining-repeating.py`](starter/shell-strings-quotes-joining-repeating.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-05/starter`
2. Read `shell-strings-quotes-joining-repeating.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   'Hello' + ' ' + 'World'
   3 * 'ab'
   len('computer')
   s = 'it\'s'
   print(s)
   print('one\ntwo')
   ```
4. Run it: `python3 -i < shell-strings-quotes-joining-repeating.py`.
5. Check it from the repository root: `./check m08l03-05`.

## Expected output

```text
'Hello World'
'ababab'
8
it's
one
two
```

## How to check

`./check m08l03-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-strings-quotes-joining-repeating.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
