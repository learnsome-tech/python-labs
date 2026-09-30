# m02l04-04 · Asking the interpreter about itself

**Lesson:** [Where Python Lives: PATH And Versions](https://learnsome.tech/learn/python-course/m02l04) (lesson 2.4, module 2: Install Python Properly) · Pro  
**Check:** Graded

## Goal

You can explain how a command name becomes a program on disk, tell python, python3 and py apart on any of the three operating systems, and ask an interpreter for its own path, version and module search path.

In the lesson: The reliable way to find out what you are running is to ask it. Import the sys module and look at four things. The executable attribute is the full path of the program running your code, which is the answer to the question, which Python is this. The version attribute is the version as a piece of text, with the build details after it. The prefix attribute is the root of the installation this interpreter belongs to. And the path list is where imports are searched for; here it has five entries, and the last of them is the folder where packages you install end up. None of that is guesswork, and none of it depends on what you think you installed.

## Files

- [`starter/shell-asking-the-interpreter-about-itself.py`](starter/shell-asking-the-interpreter-about-itself.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-04/starter`
2. Read `shell-asking-the-interpreter-about-itself.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import sys
   sys.executable
   sys.version
   sys.prefix
   len(sys.path)
   sys.path[-1]
   ```
4. Run it: `python3 -i < shell-asking-the-interpreter-about-itself.py`.
5. Check it from the repository root: `./check m02l04-04`.

## Expected output

```text
'/opt/lab/bin/python3'
'3.14.7 (main, Sep 24 2026, 17:58:18) [Clang 22.1.3 ]'
'/opt/python'
5
'/opt/python/lib/python3.14/site-packages'
```

## How to check

`./check m02l04-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-asking-the-interpreter-about-itself.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
