# m04l03-05 · Concatenation, and repetition

**Lesson:** [Strings, Delimiters And Concatenation](https://learnsome.tech/learn/python-course/m04l03) (lesson 4.3, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write string literals with either delimiter, tell a string of digits from an integer, concatenate and repeat strings, and fix the type error that mixing the two produces.

In the lesson: Strings also have operation symbols. Try the string very, noting the space after very, then a plus, then the string hot. The plus between two strings means concatenate the strings: join them end to end. Python looks at the type of the operands before deciding what operation is associated with the plus. Now think of the relation of addition and multiplication of integers, and then guess the meaning of an integer times a string. Three times the string very, with its trailing space, plus the string hot, gives very very very hot. Were you right? The ability to repeat yourself easily can be handy, and you will reach for it more often than you expect.

## Files

- [`starter/shell-concatenation-and-repetition.py`](starter/shell-concatenation-and-repetition.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-05/starter`
2. Read `shell-concatenation-and-repetition.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   'very ' + 'hot'
   3*'very ' + 'hot'
   ```
4. Run it: `python3 -i < shell-concatenation-and-repetition.py`.
5. Check it from the repository root: `./check m04l03-05`.

## Expected output

```text
'very hot'
'very very very hot'
```

## How to check

`./check m04l03-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-concatenation-and-repetition.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
