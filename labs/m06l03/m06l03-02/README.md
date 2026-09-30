# m06l03-02 · A definition with a parameter

**Lesson:** [Function Parameters](https://learnsome.tech/learn/python-course/m06l03) (lesson 6.3, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function with a parameter, call it with different arguments, and explain how a formal parameter is given the value of an actual parameter at the moment of the call.

In the lesson: The definition says that the variable name person will be used inside the function, by putting it between the parentheses of the definition heading. Then in the body, person is used in place of the real data for any specific person's name. Read, and then run, example program birthday six. In the heading, person is called a formal parameter: a placeholder for the real name of whoever is being sung to. The last two lines are the only ones outside the definitions, so they are the only ones executed directly, and each now has an actual name between the parentheses. A value supplied like that in a call is an actual parameter, or an argument. It supplies the data the function execution will use.

## Files

- [`starter/birthday6.py`](starter/birthday6.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-02/starter`
2. Read `birthday6.py` the way the lesson builds it:
   - Lines 1–7: between the parentheses
   - Lines 8–10: the last two lines
3. Notes from the lesson:
   - Line 3: person here is the formal parameter
   - Line 6: person is used in place of real data
   - Line 9: the value here is the actual parameter
4. Run it: `python3 birthday6.py`.
5. Check it from the repository root: `./check m06l03-02`.

## Expected output

```text
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Emily.
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Andre.
Happy Birthday to you!
```

## How to check

`./check m06l03-02` copies `starter/` into a scratch directory and runs `python3 birthday6.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
