# m04l03-03 · The I apostrophe m happy puzzle

**Lesson:** [Strings, Delimiters And Concatenation](https://learnsome.tech/learn/python-course/m04l03) (lesson 4.3, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write string literals with either delimiter, tell a string of digits from an integer, concatenate and repeat strings, and fix the type error that mixing the two produces.

In the lesson: Here is the puzzle the tutorial sets you. Figure out how to give Python the text I apostrophe m happy, with a full stop on the end. Use single quotes for this one and you get an error, because the apostrophe in the middle looks to Python like the end of the string, and the leftover characters make no sense. Try it with the other type of quotes and it works, and note that Python now echoes the value back inside double quotes, because the string itself contains a single quote. One more thing to know. A string can have any number of characters in it, including none. The empty string is two quote characters with nothing between them. Many beginners forget that having no characters in the middle is legal. It can be useful.

## Files

- [`starter/shell-the-i-apostrophe-m-happy-puzzle.py`](starter/shell-the-i-apostrophe-m-happy-puzzle.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-03/starter`
2. Read `shell-the-i-apostrophe-m-happy-puzzle.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   'I'm happy.'
   "I'm happy."
   ''
   ```
4. Run it: `python3 -i < shell-the-i-apostrophe-m-happy-puzzle.py`.
5. Check it from the repository root: `./check m04l03-03`.

## Expected output

```text
SyntaxError: unterminated string literal (detected at line 1)
"I'm happy."
''
```

## How to check

`./check m04l03-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-i-apostrophe-m-happy-puzzle.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
