# m15l02-04 · The format method, from chapter one

**Lesson:** [Composing Web Pages In Python](https://learnsome.tech/learn/python-course/m15l02) (lesson 15.2, module 15: Dynamic Web Pages) · Pro  
**Check:** Graded

## Goal

You can write a Python program that reads a template page from a file, formats your data into it, writes the result out and opens it in your browser.

In the lesson: Remember this program from chapter one. It asked for a name, and then built a greeting by using the string format method with the locals function, so that the piece in braces was replaced by the value of the variable of that name. Run it now and it does what it always did. That is the entire trick we are about to apply to a web page. A page is a string. If we put braces with a name inside them into the page text, the page becomes a format string, and the format method fills in the data. Nothing new to learn; we are pointing an old tool at a bigger string.

## Files

- [`starter/hello_you4.py`](starter/hello_you4.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m15l02/m15l02-04/starter`
2. Read `hello_you4.py`.
3. Run it: `python3 hello_you4.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m15l02-04`.

## Expected output

```text
Enter your name: Hello, Alice!
```

## How to check

`./check m15l02-04` copies `starter/` into a scratch directory and runs `python3 hello_you4.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m15l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
