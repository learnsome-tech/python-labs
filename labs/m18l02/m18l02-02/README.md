# m18l02-02 · A package you already have

**Lesson:** [Packages, And Your Own Library](https://learnsome.tech/learn/python-course/m18l02) (lesson 18.2, module 18: Organising Code) · Pro  
**Check:** Graded

## Goal

You can lay out a project as a package of modules with a script beside it, import between those modules with absolute imports, and run any module inside the package with the dash m switch.

In the lesson: The standard library is full of packages, so look at one. Import a package called email and ask it two questions. Its name is email, as you would expect, but the file behind it is not email dot py: it is a file called dunder init dot py. And unlike a plain module, a package has a path attribute, holding a folder to search. That is the difference, in one line. Now import one module out of it, email dot message. The module knows its own full dotted name, and the from form lets you reach in for one class and use it unqualified. Everything you learned about importing modules works on packages; there are more dots, that is all.

## Files

- [`starter/shell-a-package-you-already-have.py`](starter/shell-a-package-you-already-have.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m18l02/m18l02-02/starter`
2. Read `shell-a-package-you-already-have.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import os.path
   import email
   email.__name__
   os.path.basename(email.__file__)
   email.__path__[0].endswith('email')
   import email.message
   email.message.__name__
   from email.message import EmailMessage
   EmailMessage.__name__
   ```
4. Run it: `python3 -i < shell-a-package-you-already-have.py`.
5. Check it from the repository root: `./check m18l02-02`.

## Expected output

```text
'email'
'__init__.py'
True
'email.message'
'EmailMessage'
```

## How to check

`./check m18l02-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-a-package-you-already-have.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
