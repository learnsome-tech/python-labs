# m04l05-05 · Python is case sensitive

**Lesson:** [Literals, Identifiers And Keywords](https://learnsome.tech/learn/python-course/m04l05) (lesson 4.5, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can tell a literal from an identifier, say which character sequences Python allows as a name, avoid the reserved words, and name multi word variables in a conventional way.

In the lesson: Python is case sensitive. The identifiers last, LAST and LaSt are all different names, and using one where you meant another is a mistake Python cannot catch when both spellings happen to exist. On screen, the first two of those have been assigned different strings. Ask for lowercase last and you get Wong. Ask for the capitalised version and you get WONG, in capitals. Now ask for the one with mixed capitals and you get a name error, because that third name was never assigned anything at all. Be sure to be consistent. Using the Alt slash auto-completion shortcut in Idle helps ensure you are consistent, because it types the name for you instead of leaving you to remember how you capitalised it.

## Files

- [`starter/shell-python-is-case-sensitive.py`](starter/shell-python-is-case-sensitive.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-05/starter`
2. Read `shell-python-is-case-sensitive.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   last = 'Wong'
   LAST = 'WONG'
   last
   LAST
   LaSt
   ```
4. Run it: `python3 -i < shell-python-is-case-sensitive.py`.
5. Check it from the repository root: `./check m04l05-05`.

## Expected output

```text
'Wong'
'WONG'
Traceback (most recent call last):
NameError: name 'LaSt' is not defined. Did you mean: 'last'?
```

## How to check

`./check m04l05-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-python-is-case-sensitive.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
