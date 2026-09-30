# m13l02-10 · The in and not in operators

**Lesson:** [If Else, And Conditional Expressions](https://learnsome.tech/learn/python-course/m13l02) (lesson 13.2, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can choose between two blocks of code with an if else statement, write any of the six comparisons correctly, and test membership in a sequence with in and not in.

In the lesson: Boolean operators are not limited to numbers. A very useful one is in, which checks membership in a sequence. Start with a list of three strings. The word in asks whether that string is one of the members, and it answers with a Boolean, like every other condition. Put not in front of it, written as two words, not in, to ask the opposite question. This works on lists, on strings, and on other sequences, and it saves you writing a loop to search by hand.

## Files

- [`starter/shell-the-in-and-not-in-operators.py`](starter/shell-the-in-and-not-in-operators.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l02/m13l02-10/starter`
2. Read `shell-the-in-and-not-in-operators.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   vals = ['this', 'is', 'it']
   'is' in vals
   'was' in vals
   'is' not in vals
   'was' not in vals
   ```
4. Run it: `python3 -i < shell-the-in-and-not-in-operators.py`.
5. Check it from the repository root: `./check m13l02-10`.

## Expected output

```text
True
False
False
True
```

## How to check

`./check m13l02-10` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-in-and-not-in-operators.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
