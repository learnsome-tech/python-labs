# m06l06-04 · Passing the value on purpose

**Lesson:** [Local Scope And Global Constants](https://learnsome.tech/learn/python-course/m06l06) (lesson 6.6, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can explain why a variable created inside a function is invisible outside it, pass data between functions with parameters, and use a global constant in capitals where a global variable would be wrong.

In the lesson: If you do want local data from one function to go to another, define the called function so that it includes parameters. Read and compare and try the program goodScope. Two characters have changed. Main passes x as an argument, and f declares a parameter to receive it. Now three is printed. The x inside f is a local name in f, created by the call, and it happens to have the same value as the x in main. Nothing was made visible that was invisible before. A value was handed over deliberately, through the doorway the parameter list provides, which is the only way in.

## Files

- [`starter/goodScope.py`](starter/goodScope.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l06/m06l06-04/starter`
2. Read `goodScope.py`.
3. Notes from the lesson:
   - Line 5: the value of x is passed as an argument
   - Line 7: this x is a local name in f, made by the call
4. Run it: `python3 goodScope.py`.
5. Check it from the repository root: `./check m06l06-04`.

## Expected output

```text
3
```

## How to check

`./check m06l06-04` copies `starter/` into a scratch directory and runs `python3 goodScope.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
