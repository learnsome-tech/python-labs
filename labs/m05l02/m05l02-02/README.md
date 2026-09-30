# m05l02-02 · Reading the user's name

**Lesson:** [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) (lesson 5.2, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can read a line from the user with the input function, and convert a string of digits into a number so that arithmetic works instead of concatenation.

In the lesson: Modify the hello program like this in the editor, and save it with File, then Save As, under the name hello underscore you dot py. The first line calls input with the prompt string, and assigns whatever comes back to the variable person. The second line has that name printed with the greeting. Run the program. In the Shell you see the prompt, with the typing cursor waiting at the end of the line; make sure the cursor really is in the Shell window, type your response and press Enter. The output panel here shows only what the program printed, because the reply is fed in rather than typed, so prompt and greeting share a line.

## Files

- [`starter/hello_you.py`](starter/hello_you.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-02/starter`
2. Read `hello_you.py` the way the lesson builds it:
   - Lines 1: the prompt string
   - Lines 2: printed with the greeting
3. Run it: `python3 hello_you.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m05l02-02`.

## Expected output

```text
Enter your name: Hello Anna
```

## How to check

`./check m05l02-02` copies `starter/` into a scratch directory and runs `python3 hello_you.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
