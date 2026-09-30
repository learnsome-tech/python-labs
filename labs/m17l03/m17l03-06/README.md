# m17l03-06 · A syntax error arrives before anything runs

**Lesson:** [Reading A Traceback Like A Professional](https://learnsome.tech/learn/python-course/m17l03) (lesson 17.3, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can read a multi-frame traceback bottom up, tell your own frames from a library's, recognise the errors that arrive before execution starts, and name the likely cause behind each of the common exception types.

In the lesson: Here is a different animal altogether. There is a colon missing at the end of the for statement. Run the program, and look at what is missing from the report. There is no heading about the most recent call, and there is only one File line, with a line number but no function name. That is because nothing ran. The interpreter has to read the whole file before it can execute any of it, and it never got past line two, so there were no calls to list and no frames to print. A caret points at the exact spot where the interpreter's patience ran out, and expected a colon says what it wanted to see there.

## Files

- [`starter/badsyntax.py`](starter/badsyntax.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

`starter/badsyntax.py` does not parse, on purpose: the lesson shows the error it gives.

## Steps

1. Go to the starter: `cd labs/m17l03/m17l03-06/starter`
2. Read `badsyntax.py`.
3. Run it: `python3 badsyntax.py`.
4. Check it from the repository root: `./check m17l03-06`.

## Expected output

```text
  File "badsyntax.py", line 2
    for score in scores
                       ^
SyntaxError: expected ':'
```

## How to check

`./check m17l03-06` copies `starter/` into a scratch directory and runs `python3 badsyntax.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
