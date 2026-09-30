# m05l02-03 · Three inputs in sequence

**Lesson:** [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) (lesson 5.2, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can read a line from the user with the input function, and convert a string of digits into a number so that arithmetic works instead of concatenation.

In the lesson: Open the example program interview dot py, and before running it, see if you can predict what it will do. There are three separate calls to input, each with its own prompt and its own variable, and then one print function assembling a sentence. Notice the prompts use double quotes, because the text inside contains an apostrophe. The important idea is order: the statements are executed in the order they appear in the text of the program, one after another. That is sequential execution, the simplest way for the flow of a program to run. Later you will meet instructions that alter that natural flow.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/interview.py`](starter/interview.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-03/starter`
2. Read `interview.py` the way the lesson builds it:
   - Lines 1–5: three separate calls
   - Lines 6: one print function
3. Run it: `python3 interview.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m05l02-03`.

## Expected output

```text
Enter the applicant's name: Enter the interviewer's name: Enter the appointment time: Bob Jones will interview Anna Smith at 2:30 pm
```

## How to check

`./check m05l02-03` copies `starter/` into a scratch directory and runs `python3 interview.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
