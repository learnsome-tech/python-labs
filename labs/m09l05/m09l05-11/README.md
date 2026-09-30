# m09l05-11 · Constructors in the shell

**Lesson:** [Appending To Lists, Sets, Constructors](https://learnsome.tech/learn/python-course/m09l05) (lesson 9.5, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can grow a list with append inside a loop, explain why that differs from concatenation, build a set to remove duplicates, and recognise a type name used as a constructor.

In the lesson: Take them one at a time in the shell so you can see the types in the answers. The integer constructor turns the digits into a number, and the shell shows it as a number now, with no quotes around it. The string constructor turns the number back into text, and the quotes are back to prove it. An empty list shows as empty brackets, and an empty dictionary shows as empty braces, which is worth remembering, because braces mean both dictionary and set. An empty set has to be written by calling set, since empty braces are already taken by the dictionary.

## Files

- [`starter/shell-constructors-in-the-shell.py`](starter/shell-constructors-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l05/m09l05-11/starter`
2. Read `shell-constructors-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   x = int('123')
   x
   s = str(123)
   s
   nums = list()
   nums
   d = dict()
   d
   ```
4. Run it: `python3 -i < shell-constructors-in-the-shell.py`.
5. Check it from the repository root: `./check m09l05-11`.

## Expected output

```text
123
'123'
[]
{}
```

## How to check

`./check m09l05-11` copies `starter/` into a scratch directory and runs `python3 -i < shell-constructors-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
