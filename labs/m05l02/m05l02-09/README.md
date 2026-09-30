# m05l02-09 · Converting the input explicitly

**Lesson:** [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) (lesson 5.2, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can read a line from the user with the input function, and convert a string of digits into a number so that arithmetic works instead of concatenation.

In the lesson: So we convert. The example file addition two dot py introduces extra variable names deliberately, to keep the two kinds of value apart. The name ending in string holds the string the user typed, and the short name holds the integer that int gives back. Read it and run it: now the sentence is right, and the sum of two and three is five. State the lesson plainly, because you will need it constantly, with keyboard input and later with data arriving from web pages. Input arrives as text. To calculate with it, you must convert it first.

## Files

- [`starter/addition2.py`](starter/addition2.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-09/starter`
2. Read `addition2.py` the way the lesson builds it:
   - Lines 1–4: the string the user typed
   - Lines 5–7: the sentence is right
3. Run it: `python3 addition2.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m05l02-09`.

## Expected output

```text
Enter a number: Enter a second number: The sum of 2 and 3 is 5.
```

## How to check

`./check m05l02-09` copies `starter/` into a scratch directory and runs `python3 addition2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
