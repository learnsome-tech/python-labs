# m02l02-10 · Ask Python itself, not the internet

**Lesson:** [Installing Python On A Mac](https://learnsome.tech/learn/python-course/m02l02) (lesson 2.2, module 2: Install Python Properly) · Pro  
**Check:** Graded

## Goal

You can install your own Python on a Mac by either the python.org installer or Homebrew, leave Apple's system python3 untouched, put yours first on PATH from your zsh profile, and confirm the result with python3 and idle3.

In the lesson: When something goes wrong later, this tiny program is the first thing to run, because it makes your Python answer for itself rather than you reading advice about somebody else's Mac. Import the sys module. Then print three facts. The version, as a tuple of separate numbers, so your own code can ask a real question about it. The executable, the full path of the binary running this program. And the prefix, the root of the tree it loads its library from. On my machine all three point at Homebrew. Yours will differ, and that is fine, so long as they agree with the route you chose.

## Files

- [`starter/pyfacts.py`](starter/pyfacts.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-10/starter`
2. Read `pyfacts.py` the way the lesson builds it:
   - Lines 1: Import the sys module
   - Lines 2–3: three facts
   - Lines 4–5: And the prefix
3. Notes from the lesson:
   - Line 3: version_info: major, minor and micro as separate numbers
   - Line 4: sys.executable is the exact binary running this program
   - Line 5: sys.prefix is the tree it loads its library from
4. Run it: `python3 pyfacts.py`.
5. Check it from the repository root: `./check m02l02-10`.

## Expected output

```text
(3, 14, 7)
/opt/lab/bin/python3
/opt/python
```

## How to check

`./check m02l02-10` copies `starter/` into a scratch directory and runs `python3 pyfacts.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. undefined A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
