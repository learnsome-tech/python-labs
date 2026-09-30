# m16l01-02 · A program with planned errors

**Lesson:** [Reading Error Messages](https://learnsome.tech/learn/python-course/m16l01) (lesson 16.1, module 16: Reading Errors, And Platform Notes) · Pro  
**Check:** Graded

## Goal

You can tell a syntax error from a run time error, read a traceback from the bottom up, and follow the chain of calls above the failing line to your own code.

In the lesson: Here is a program written to be wrong, from the examples folder. In the file itself there is a documentation line and a stack of blank lines above these four, so that Idle's pop up window does not hide the code. That padding is why the line numbers in your own copy come out twelve larger than the ones on screen here. Run it as it stands. Nothing executes. In Idle you get a pop up saying there is an error, and after you click on it the place where the interpreter noticed is highlighted. From a terminal you see what is on screen. The message says an unterminated string literal, and points at the last line: a string literal was opened and the line ended before a closing quote arrived.

## Files

- [`starter/BADexamplecode.py`](starter/BADexamplecode.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

`starter/BADexamplecode.py` does not parse, on purpose: the lesson shows the error it gives.

## Steps

1. Go to the starter: `cd labs/m16l01/m16l01-02/starter`
2. Read `BADexamplecode.py`.
3. Run it: `python3 BADexamplecode.py`.
4. Check it from the repository root: `./check m16l01-02`.

## Expected output

```text
  File "BADexamplecode.py", line 4
    print('Now we are done!)
          ^
SyntaxError: unterminated string literal (detected at line 4)
```

## How to check

`./check m16l01-02` copies `starter/` into a scratch directory and runs `python3 BADexamplecode.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m16l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
