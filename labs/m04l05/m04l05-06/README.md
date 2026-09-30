# m04l05-06 · Hiding a predefined name is legal, and unwise

**Lesson:** [Literals, Identifiers And Keywords](https://learnsome.tech/learn/python-course/m04l05) (lesson 4.5, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can tell a literal from an identifier, say which character sequences Python allows as a name, avoid the reserved words, and name multi word variables in a conventional way.

In the lesson: Reserved words are refused outright. Predefined names are a different matter: Python lets you take them over. Name your own variable list, and the assignment goes through without a murmur. Ask for it and your own value comes back. But now try to use the predefined function that is also called list, the one that builds a list out of a range, and you get a type error saying a list object is not callable. You have not broken Python. You have hidden one of its names behind one of yours, for as long as this shell session lasts. It is perfectly legal, and it is a poor idea. Idle colours predefined names differently, and that colour is your warning to pick another word.

## Files

- [`starter/shell-hiding-a-predefined-name-is-legal-and-unwise.py`](starter/shell-hiding-a-predefined-name-is-legal-and-unwise.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-06/starter`
2. Read `shell-hiding-a-predefined-name-is-legal-and-unwise.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   list = [1, 2]
   list
   list(range(3))
   ```
4. Run it: `python3 -i < shell-hiding-a-predefined-name-is-legal-and-unwise.py`.
5. Check it from the repository root: `./check m04l05-06`.

## Expected output

```text
[1, 2]
Traceback (most recent call last):
TypeError: 'list' object is not callable
```

## How to check

`./check m04l05-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-hiding-a-predefined-name-is-legal-and-unwise.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
