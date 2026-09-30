# m06l06-02 · A local name that will not travel

**Lesson:** [Local Scope And Global Constants](https://learnsome.tech/learn/python-course/m06l06) (lesson 6.6, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can explain why a variable created inside a function is invisible outside it, pass data between functions with parameters, and use a global constant in capitals where a global variable would be wrong.

In the lesson: Here is the error that follows from that rule, in example program badScope. Read it and run it, and see. The function main gives the name x the value three, and then calls f. The function f tries to print x. It fails. The name x is local to main, so from inside f it does not exist, and Python raises a NameError saying that the name x is not defined. Read the traceback and it takes you to the print statement inside f. This is not Python being unhelpful. If a function could reach into the local names of whoever called it, then renaming a variable inside one function could break another, and nobody could write a function safely.

## Files

- [`starter/badScope.py`](starter/badScope.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l06/m06l06-02/starter`
2. Read `badScope.py`.
3. Notes from the lesson:
   - Line 4: x is local to main
   - Line 8: f has no idea that any x exists
4. Run it: `python3 badScope.py`.
5. Check it from the repository root: `./check m06l06-02`.

## Expected output

```text
Traceback (most recent call last):
NameError: name 'x' is not defined
```

## How to check

`./check m06l06-02` copies `starter/` into a scratch directory and runs `python3 badScope.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
