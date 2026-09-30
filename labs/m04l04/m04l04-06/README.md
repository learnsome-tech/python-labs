# m04l04-06 · Width is assigned width plus five

**Lesson:** [Variables And Assignment](https://learnsome.tech/learn/python-course/m04l04) (lesson 4.4, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can write assignment statements, explain why the right hand side is evaluated first, and tell a syntax error apart from a name error found while a line is running.

In the lesson: Set width back to ten, and then try a line with the same name on both sides: width is assigned width plus five. This is, of course, nonsensical as mathematics, since no number is equal to itself plus five, but it makes perfectly good sense as an assignment, with the right hand side calculated first. Can you figure out the value that is now associated with width? Check by entering the name again. The answer is fifteen. In the assignment statement, the expression on the right is evaluated first. At that point width was associated with its original value, ten, so width plus five had the value of ten plus five, which is fifteen. That value was then assigned to the variable on the left, width again, to give it a new value. We will modify the value of variables in a similar way routinely.

## Files

- [`starter/shell-width-is-assigned-width-plus-five.py`](starter/shell-width-is-assigned-width-plus-five.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-06/starter`
2. Read `shell-width-is-assigned-width-plus-five.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   width = 10
   width = width + 5
   width
   ```
4. Run it: `python3 -i < shell-width-is-assigned-width-plus-five.py`.
5. Check it from the repository root: `./check m04l04-06`.

## Expected output

```text
15
```

## How to check

`./check m04l04-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-width-is-assigned-width-plus-five.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
