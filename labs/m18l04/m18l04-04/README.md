# m18l04-04 · Where the files actually go

**Lesson:** [pip, requirements, and installing packages](https://learnsome.tech/learn/python-course/m18l04) (lesson 18.4, module 18: Organising Code) · Pro  
**Check:** Graded

## Goal

You can install, inspect and remove packages with pip inside an activated environment, pin them in a requirements file that rebuilds the environment anywhere, and read the externally managed environment error correctly.

In the lesson: You do not have to guess where a package went; you can ask Python itself. The last entry of the search path is always the site-packages folder, the last place searched, and that is where pip writes. Run this with your ordinary Python, outside any environment, and you see the folder name and a false for the environment question. Run the same program with your environment active and the folder is the one inside your dot venv, so the same import statement finds different code depending on which python you started. That is the entire mechanism. Alongside each installed package pip writes a small folder ending in dist dash info, holding the version number and the list of files, which is what makes a clean uninstall possible.

## Files

- [`starter/wherepackages.py`](starter/wherepackages.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m18l04/m18l04-04/starter`
2. Read `wherepackages.py`.
3. Notes from the lesson:
   - Line 6: the last place on the import search path
4. Run it: `python3 wherepackages.py`.
5. Check it from the repository root: `./check m18l04-04`.

## Expected output

```text
last folder searched: site-packages
inside a virtual environment: False
```

## How to check

`./check m18l04-04` copies `starter/` into a scratch directory and runs `python3 wherepackages.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
