# m05l02-11 · Input, calculate, output

**Lesson:** [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) (lesson 5.2, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can read a line from the user with the input function, and convert a string of digits into a number so that arithmetic works instead of concatenation.

In the lesson: One more variation, addition four dot py, our reference version. It asks for integers, and it names the answer. The simple programs so far have all followed a basic programming pattern: input, calculate, output. Get all the data first, calculate with it second, and output the results last. That sequence is clearer when you create a named result variable in the middle, as this program does with the variable called sum. The file now reads like the structure of the task, starting from the documentation string at the top. See the sentence come out the same, and hold on to this shape.

## Files

- [`starter/addition4.py`](starter/addition4.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-11/starter`
2. Read `addition4.py` the way the lesson builds it:
   - Lines 1–2: the documentation string
   - Lines 3–4: get all the data first
   - Lines 5–6: output the results last
3. Run it: `python3 addition4.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m05l02-11`.

## Expected output

```text
Enter an integer: Enter another integer: The sum of 2 and 3 is 5.
```

## How to check

`./check m05l02-11` copies `starter/` into a scratch directory and runs `python3 addition4.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
