# m18l03-06 · Asking Python where it is

**Lesson:** [Virtual Environments](https://learnsome.tech/learn/python-course/m18l03) (lesson 18.3, module 18: Organising Code) · Pro  
**Check:** Graded

## Goal

You can create a virtual environment for a project, activate and deactivate it on your own operating system, explain what activation does to PATH, and check from inside Python whether you are in one.

In the lesson: There is a definitive test, and it is two attributes of the sys module. Sys dot prefix is the root of the Python that is running. Sys dot base prefix is the root of the one it was built from. Outside an environment those are the same folder, so run this with your ordinary Python and it says the prefixes agree. Inside an activated environment, prefix points at your dot venv folder while base prefix still points at the installed Python, the one it was built from, so they differ and the comparison is false. That is how tools tell. When you are not sure which Python is really running, print sys dot executable as well, and it will tell you the exact file.

## Files

- [`starter/whichpython.py`](starter/whichpython.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m18l03/m18l03-06/starter`
2. Read `whichpython.py`.
3. Notes from the lesson:
   - Line 5: prefix: this interpreter; base prefix: the one it was built from
4. Run it: `python3 whichpython.py`.
5. Check it from the repository root: `./check m18l03-06`.

## Expected output

```text
prefix and base prefix agree: True
so this is not a virtual environment
```

## How to check

`./check m18l03-06` copies `starter/` into a scratch directory and runs `python3 whichpython.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
