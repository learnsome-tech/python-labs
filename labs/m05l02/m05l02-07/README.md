# m05l02-07 · The addition that does not add

**Lesson:** [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) (lesson 5.2, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can read a line from the user with the input function, and convert a string of digits into a number so that arithmetic works instead of concatenation.

In the lesson: Now a new problem: prompt the user for two numbers, then print a sentence stating their sum. You might imagine a solution like the example file addition one dot py. There is a problem. Can you figure it out before you run it? The hint is that the input function produces values of string type. End up running it in any case and look at the answer: with two and three typed in, the sentence claims the sum is twenty-three. That is not integer addition but string concatenation, because both x and y are strings of digits, and plus on two strings joins them end to end.

## Files

- [`starter/addition1.py`](starter/addition1.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-07/starter`
2. Read `addition1.py`.
3. Notes from the lesson:
   - Line 5: x and y are strings, so plus concatenates instead of adding
4. Run it: `python3 addition1.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m05l02-07`.

## Expected output

```text
Enter a number: Enter a second number: The sum of 2 and 3 is 23.
```

## How to check

`./check m05l02-07` copies `starter/` into a scratch directory and runs `python3 addition1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
