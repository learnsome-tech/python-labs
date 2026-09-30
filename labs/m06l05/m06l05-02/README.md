# m06l05-02 · The return statement

**Lesson:** [Returning Values](https://learnsome.tech/learn/python-course/m06l05) (lesson 6.5, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function that returns a value, use a call inside a larger expression, and tell the difference between a function that prints and a function that returns.

In the lesson: Here is the same definition and the same examples in Python, from example program return one. Read and run it. The new syntax is the return statement: the word return followed by an expression. Functions that return values can be used in expressions, just as in the algebra class. When an expression containing a call is evaluated, the call is effectively replaced by the returned value. Inside the definition, the value to be returned is given by the expression in the return statement, here x times x. The first print shows nine. The second adds two calls together and shows twenty-five, without either call printing anything itself.

## Files

- [`starter/return1.py`](starter/return1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-02/starter`
2. Read `return1.py` the way the lesson builds it:
   - Lines 1–4: the word return followed by an expression
   - Lines 5–7: used in expressions
3. Notes from the lesson:
   - Line 4: the value handed back to the caller
   - Line 7: two calls inside one larger expression
4. Run it: `python3 return1.py`.
5. Check it from the repository root: `./check m06l05-02`.

## Expected output

```text
9
25
```

## How to check

`./check m06l05-02` copies `starter/` into a scratch directory and runs `python3 return1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
