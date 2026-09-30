# m06l03-06 · The name comes from the keyboard

**Lesson:** [Function Parameters](https://learnsome.tech/learn/python-course/m06l03) (lesson 6.3, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function with a parameter, call it with different arguments, and explain how a formal parameter is given the value of an actual parameter at the moment of the call.

In the lesson: We can combine function parameters with user input, and print Happy Birthday for anyone. Check out the main function of birthday who, and run it. There are now two different ways information gets into a function. A value can be passed in through a parameter, from the call in main to the heading of happyBirthday. Or the user can be prompted and the data read from the keyboard. It is a good idea to separate the internal processing of data from the external input from the user, using distinct functions, and that is what is done here: the user interaction is in main, and the data is manipulated in happyBirthday.

## Files

- [`starter/birthday_who.py`](starter/birthday_who.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-06/starter`
2. Read `birthday_who.py`.
3. Notes from the lesson:
   - Line 10: user interaction lives in main
   - Line 11: the value of userName becomes the value of person
4. Run it: `python3 birthday_who.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m06l03-06`.

## Expected output

```text
Enter the Birthday person's name: Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Maria.
Happy Birthday to you!
```

## How to check

`./check m06l03-06` copies `starter/` into a scratch directory and runs `python3 birthday_who.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
