# m17l03-08 · The nine you will meet again and again

**Lesson:** [Reading A Traceback Like A Professional](https://learnsome.tech/learn/python-course/m17l03) (lesson 17.3, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can read a multi-frame traceback bottom up, tell your own frames from a library's, recognise the errors that arrive before execution starts, and name the likely cause behind each of the common exception types.

In the lesson: Nine exception types cover most of what a beginner meets, so here they are, one line each, with only the last line of each traceback shown. A name that nothing has been assigned to gives NameError. An operation on the wrong sorts of things gives TypeError. The right sort of thing with an unusable value gives ValueError. A position past the end of a list gives IndexError, and a key that is not in the dictionary gives KeyError. Asking an object for a method it has not got gives AttributeError. A divisor that turned out to be zero gives ZeroDivisionError. Importing no such module gives ModuleNotFoundError, a kind of ImportError; this one was removed from the standard library in Python three point thirteen. And opening a path that is not there gives FileNotFoundError.

## Files

- [`starter/shell-the-nine-you-will-meet-again-and-again.py`](starter/shell-the-nine-you-will-meet-again-and-again.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l03/m17l03-08/starter`
2. Read `shell-the-nine-you-will-meet-again-and-again.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   total
   '3' + 4
   int('3.5')
   [10, 20, 30][3]
   {'a': 1}['b']
   'hello'.push('x')
   7 / 0
   import cgi
   open('nosuch.txt')
   ```
4. Run it: `python3 -i < shell-the-nine-you-will-meet-again-and-again.py`.
5. Check it from the repository root: `./check m17l03-08`.

## Expected output

```text
NameError: name 'total' is not defined
TypeError: can only concatenate str (not "int") to str
ValueError: invalid literal for int() with base 10: '3.5'
IndexError: list index out of range
KeyError: 'b'
AttributeError: 'str' object has no attribute 'push'
ZeroDivisionError: division by zero
ModuleNotFoundError: No module named 'cgi'
FileNotFoundError: [Errno 2] No such file or directory: 'nosuch.txt'
```

## How to check

`./check m17l03-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-nine-you-will-meet-again-and-again.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
