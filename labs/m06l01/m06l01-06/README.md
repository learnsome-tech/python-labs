# m06l01-06 · A definition and two calls

**Lesson:** [Defining Your First Function](https://learnsome.tech/learn/python-course/m06l01) (lesson 6.1, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function definition with def, an indented body and a call, and explain why defining a function is not the same as running it.

In the lesson: Example file birthday three adds two more lines, and neither of them is indented. Can you guess what it does? At the top is a docstring, a string on a line of its own that documents the file. Then comes the definition, then a blank line, then two calls. Run it, and the song comes out twice. Two points to notice. The blank line after the body is there for human eyes; what really ends the definition is the indentation ending. And the two calls at the bottom sit outside the definition, so they are the only lines executed directly. Each one sends execution into the function and gets it back afterwards.

## Files

- [`starter/birthday3.py`](starter/birthday3.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-06/starter`
2. Read `birthday3.py` the way the lesson builds it:
   - Lines 1–7: the definition
   - Lines 8–10: two calls
3. Notes from the lesson:
   - Line 9: not indented, so this line is executed directly
4. Run it: `python3 birthday3.py`.
5. Check it from the repository root: `./check m06l01-06`.

## Expected output

```text
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Emily.
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear Emily.
Happy Birthday to you!
```

## How to check

`./check m06l01-06` copies `starter/` into a scratch directory and runs `python3 birthday3.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
