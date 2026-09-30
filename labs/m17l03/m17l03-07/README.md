# m17l03-07 · IndentationError, its close relative

**Lesson:** [Reading A Traceback Like A Professional](https://learnsome.tech/learn/python-course/m17l03) (lesson 17.3, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can read a multi-frame traceback bottom up, tell your own frames from a library's, recognise the errors that arrive before execution starts, and name the likely cause behind each of the common exception types.

In the lesson: The same thing happens with indentation. The second line of this function body has drifted two spaces to the right, and Python has no way to guess what that block is meant to be. So again nothing runs, and nothing is printed, not even the hello you can plainly see. An IndentationError is a kind of SyntaxError, reported the same way and at the same moment. Here is the practical difference to hold on to: if you see the heading about calls and a chain of frames, your program was running. If you see a single File line and no frames, it never started.

## Files

- [`starter/badindent.py`](starter/badindent.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

`starter/badindent.py` does not parse, on purpose: the lesson shows the error it gives.

## Steps

1. Go to the starter: `cd labs/m17l03/m17l03-07/starter`
2. Read `badindent.py`.
3. Run it: `python3 badindent.py`.
4. Check it from the repository root: `./check m17l03-07`.

## Expected output

```text
  File "badindent.py", line 3
    print('goodbye', name)
IndentationError: unexpected indent
```

## How to check

`./check m17l03-07` copies `starter/` into a scratch directory and runs `python3 badindent.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
