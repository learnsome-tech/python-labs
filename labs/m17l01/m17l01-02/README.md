# m17l01-02 · With no handler at all, the program dies

**Lesson:** [Exceptions: try, except, else, finally](https://learnsome.tech/learn/python-course/m17l01) (lesson 17.1, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can wrap risky work in a try statement, catch the particular exception it may raise, use the as clause, else and finally correctly, and keep a program alive through bad input.

In the lesson: Two harmless lines. Run it and type the word twelve at the prompt. The int function is handed a string it cannot possibly turn into a number, so it raises a ValueError, and since nothing here is prepared to handle one, that is the end of the program. The second line never runs. As in the last module, we are running from a terminal with the answer piped in, so the prompt and the first traceback line have ended up on one line. Read the bottom line. The name before the colon is the type of the exception, and what follows the colon is the message it carries.

## Files

- [`starter/agecrash.py`](starter/agecrash.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l01/m17l01-02/starter`
2. Read `agecrash.py`.
3. Run it: `python3 agecrash.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m17l01-02`.

## Expected output

```text
Your age: Traceback (most recent call last):
  File "agecrash.py", line 1, in <module>
    age = int(input('Your age: '))
ValueError: invalid literal for int() with base 10: 'twelve'
```

## How to check

`./check m17l01-02` copies `starter/` into a scratch directory and runs `python3 agecrash.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
