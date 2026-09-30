# m05l02-05 · The print keyword parameter sep

**Lesson:** [Input, And Numbers Versus Digits](https://learnsome.tech/learn/python-course/m05l02) (lesson 5.2, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can read a line from the user with the input function, and convert a string of digits into a number so that arithmetic works instead of concatenation.

In the lesson: Here is the other approach, in the example file hello underscore you two dot py. Instead of joining with plus, we change the separator that the print function puts between fields. This introduces keyword parameters. The print function has one named sep, short for the separator. Leave it out, as we have so far, and it is set equal to a single space by default. Add a final field giving sep the empty string, and print puts nothing at all between the fields. It is the same two statements as before, with the spaces we do want written into the strings themselves. Try the program: the punctuation now sits against the name.

## Files

- [`starter/hello_you2.py`](starter/hello_you2.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-05/starter`
2. Read `hello_you2.py` the way the lesson builds it:
   - Lines 1–4: the same two statements
   - Lines 5: a final field
3. Notes from the lesson:
   - Line 5: sep is the separator printed between fields; here, nothing at all
4. Run it: `python3 hello_you2.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m05l02-05`.

## Expected output

```text
Enter your name: Hello Anna!
```

## How to check

`./check m05l02-05` copies `starter/` into a scratch directory and runs `python3 hello_you2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
