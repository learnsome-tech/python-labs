# m16l01-10 · A traceback with a chain of calls

**Lesson:** [Reading Error Messages](https://learnsome.tech/learn/python-course/m16l01) (lesson 16.1, module 16: Reading Errors, And Platform Notes) · Pro  
**Check:** Graded

## Goal

You can tell a syntax error from a run time error, read a traceback from the bottom up, and follow the chain of calls above the failing line to your own code.

In the lesson: In the last program the error happened outside any function call. This silly example shows what a traceback looks like when the error is inside one. The first call, with six, is fine: one divided by six take four is nought point five. The second call, with four, divides by zero. Now look at the traceback. After its title line there are three indented lines starting with the word File, not just one. The bottom one shows the line where the error actually occurred, and the last line of all names the error itself.

## Files

- [`starter/showtraceback.py`](starter/showtraceback.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m16l01/m16l01-10/starter`
2. Read `showtraceback.py`.
3. Run it: `python3 showtraceback.py`.
4. Check it from the repository root: `./check m16l01-10`.

## Expected output

```text
This program is INTENDED to cause an execution error.
Ok call to invminus4(6) next:
0.5
Bad call invminus4(4) next:
Traceback (most recent call last):
  File "showtraceback.py", line 14, in <module>
    main()
    ~~~~^^
  File "showtraceback.py", line 11, in main
    print(invminus4(4))
          ~~~~~~~~~^^^
  File "showtraceback.py", line 4, in invminus4
    return 1.0/(x-4)
           ~~~^^~~~~
ZeroDivisionError: division by zero
```

## How to check

`./check m16l01-10` copies `starter/` into a scratch directory and runs `python3 showtraceback.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m16l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
