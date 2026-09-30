# m13l06-02 · startswith and endswith

**Lesson:** [More String Methods](https://learnsome.tech/learn/python-course/m13l06) (lesson 13.6, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can test what a string starts with, ends with or is made of, and build up conditions from string methods such as startswith, endswith, replace and isdigit.

In the lesson: Try these in the shell. A minus sign at the front gives True, and so does a whole word at the front, because the piece you pass can be any length. But a minus sign anywhere else in the string does not count: these methods look only at the very beginning. Ends with is the mirror image, testing the ending instead. Notice how the answers are already Boolean values, so any of these lines could be dropped straight into an if heading without a comparison anywhere in sight.

## Files

- [`starter/shell-startswith-and-endswith.py`](starter/shell-startswith-and-endswith.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l06/m13l06-02/starter`
2. Read `shell-startswith-and-endswith.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   '-123'.startswith('-')
   'downstairs'.startswith('down')
   '1 - 2 - 3'.startswith('-')
   'whoever'.endswith('ever')
   'downstairs'.endswith('airs')
   '1 - 2 - 3'.endswith('-')
   ```
4. Run it: `python3 -i < shell-startswith-and-endswith.py`.
5. Check it from the repository root: `./check m13l06-02`.

## Expected output

```text
True
True
False
True
True
False
```

## How to check

`./check m13l06-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-startswith-and-endswith.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
