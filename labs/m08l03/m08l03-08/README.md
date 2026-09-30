# m08l03-08 · Defining and calling functions

**Lesson:** [Chapter One In One Sitting](https://learnsome.tech/learn/python-course/m08l03) (lesson 8.3, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can recall, in one sitting, every idea from chapter one: the types and their literals, variables, operators and precedence, strings and formatting, input and output, functions, dictionaries, loops and floats.

In the lesson: Group six: functions, and the shape of a whole module. A file may start with a documentation string describing it, and a function may start with one describing its return value and anything the parameter names do not make obvious. The def heading gives a name, a parenthesised list of parameters, and a colon, then an indented block. Defining runs nothing; the lines are only remembered. Calling passes actual parameters, in order, into fresh local variables, which vanish when the call ends. A return statement ends the call immediately and hands its value back where the call was written. By convention the work lives in a function called main, and the only line that does anything at the outer level is the call to it.

## Files

- [`starter/summaryFunc.py`](starter/summaryFunc.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-08/starter`
2. Read `summaryFunc.py` the way the lesson builds it:
   - Lines 1–3: a documentation string
   - Lines 4–7: the def heading
   - Lines 8–11: a function called main
   - Lines 12–13: the only line that does anything
3. Run it: `python3 summaryFunc.py`.
4. Check it from the repository root: `./check m08l03-08`.

## Expected output

```text
10 costs 12.00
25 costs 30.00
```

## How to check

`./check m08l03-08` copies `starter/` into a scratch directory and runs `python3 summaryFunc.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
