# m06l03-05 · Parameters and a main function together

**Lesson:** [Function Parameters](https://learnsome.tech/learn/python-course/m06l03) (lesson 6.3, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function with a parameter, call it with different arguments, and explain how a formal parameter is given the value of an actual parameter at the moment of the call.

In the lesson: You can go back to having a main function again, and everything works. Run birthday seven. There is one distinction to make between this version and the last. In birthday six the two calls were outside any definition, so they led to immediate execution of the function. Here the calls to happyBirthday sit inside another function definition, main, so they are not run when they are read. They are run only when main itself is run, from the last line, which is outside every definition. Two levels of the same rule, in one small file.

## Files

- [`starter/birthday7.py`](starter/birthday7.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-05/starter`
2. Read `birthday7.py`.
3. Notes from the lesson:
   - Line 10: inside main, so not run until main is called
4. Run it: `python3 birthday7.py`.
5. Check it from the repository root: `./check m06l03-05`.

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

`./check m06l03-05` copies `starter/` into a scratch directory and runs `python3 birthday7.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
