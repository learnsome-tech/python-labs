# m08l03-07 · Input, conversion and output

**Lesson:** [Chapter One In One Sitting](https://learnsome.tech/learn/python-course/m08l03) (lesson 8.3, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can recall, in one sitting, every idea from chapter one: the types and their literals, variables, operators and precedence, strings and formatting, input and output, functions, dictionaries, loops and floats.

In the lesson: Group five: input and output, and the simplest program shape, input, calculate, output. The input function prints its prompt, waits for a line from the keyboard, and returns what was typed, always a string. For arithmetic, convert it, using a type name as a function, as on the second line. The print function shows the value of each expression it is given, separated by single blanks, and ends with a newline, unless you change either with the keyword arguments sep and end. Called with nothing it just moves to a new line. Run it with a name and an age: the two prompts sit on the same line as the answer, because a prompt has no newline of its own.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/summaryIO.py`](starter/summaryIO.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-07/starter`
2. Read `summaryIO.py` the way the lesson builds it:
   - Lines 1–2: always a string
   - Lines 3–4: separated by single blanks
3. Run it: `python3 summaryIO.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m08l03-07`.

## Expected output

```text
Name: Age: Hello, Ann you turn 31 next year.
Rounded to a penny: 19.99
```

## How to check

`./check m08l03-07` copies `starter/` into a scratch directory and runs `python3 summaryIO.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
