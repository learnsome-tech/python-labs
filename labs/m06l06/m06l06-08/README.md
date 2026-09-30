# m06l06-08 · The same constant, in the Shell

**Lesson:** [Local Scope And Global Constants](https://learnsome.tech/learn/python-course/m06l06) (lesson 6.6, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can explain why a variable created inside a function is invisible outside it, pass data between functions with parameters, and use a global constant in capitals where a global variable would be wrong.

In the lesson: You can build the same thing in the Shell, a piece at a time, and watch the constant do its work. PI is assigned once. Then the area function is defined, using PI inside its body although nothing was passed to it, and calling it with a radius of five gives the area you see. Then the circumference function is defined in the same way, and the second answer comes back for the same radius. Neither function was told what PI is. Each one reached out to the name defined at the top level, which is what global scope means. Those are the two numbers the program prints, next to their labels.

## Files

- [`starter/shell-the-same-constant-in-the-shell.py`](starter/shell-the-same-constant-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l06/m06l06-08/starter`
2. Read `shell-the-same-constant-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   PI = 3.14159265358979
   def circleArea(radius):
       return PI*radius*radius
   circleArea(5)
   def circleCircumference(radius):
       return 2*PI*radius
   circleCircumference(5)
   ```
4. Run it: `python3 -i < shell-the-same-constant-in-the-shell.py`.
5. Check it from the repository root: `./check m06l06-08`.

## Expected output

```text
78.53981633974475
31.4159265358979
```

## How to check

`./check m06l06-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-same-constant-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
