# m05l02-10 · Converting immediately

**Lesson:** [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) (lesson 5.2, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can read a line from the user with the input function, and convert a string of digits into a number so that arithmetic works instead of concatenation.

In the lesson: Those extra variables emphasised the steps, but it is more concise to convert immediately, as in the example file addition three dot py. The call to input sits inside the call to int. Read it from the inside out: input prints the prompt and returns a string, and int is handed that string and returns an integer, which is what gets assigned. It is exactly the same result as before with two statements fewer, and this is the form you will meet most often. Get comfortable reading nested calls this way.

## Files

- [`starter/addition3.py`](starter/addition3.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-10/starter`
2. Read `addition3.py`.
3. Notes from the lesson:
   - Line 3: the inner call returns a string; int converts it on the spot
4. Run it: `python3 addition3.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m05l02-10`.

## Expected output

```text
Enter a number: Enter a second number: The sum of 2 and 3 is 5.
```

## How to check

`./check m05l02-10` copies `starter/` into a scratch directory and runs `python3 addition3.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
