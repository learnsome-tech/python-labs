# m04l06-06 · The literal above, the printed form below

**Lesson:** [The Print Function And String Literals](https://learnsome.tech/learn/python-course/m04l06) (lesson 4.6, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can display anything you like with the print function, write a string literal that spans several lines, and read the escape codes that stand for a newline, a quote or a backslash.

In the lesson: Put the same idea in a file, where the difference is unmistakable. The literal on the first line is one line of source text containing two escape codes: a backslash before the apostrophe, so the apostrophe does not end the string, and a backslash n where the line break belongs. The plain double quote characters need no escaping inside a single quoted string. Printing it turns the codes into their meanings, so the output shows two lines, with a real apostrophe and real double quotes. The third line of the program prints a lone backslash, written in the source as two of them. Run the file and compare the two panels: three lines of source, three lines of output, but not the same three. The literal and the printed form are different text, and confusing them is a common early mistake.

## Files

- [`starter/escapes.py`](starter/escapes.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l06/m04l06-06/starter`
2. Read `escapes.py` the way the lesson builds it:
   - Lines 1: the literal on the first line
   - Lines 2: printing it turns the codes
   - Lines 3: a lone backslash
3. Notes from the lesson:
   - Line 1: backslash apostrophe, and backslash n where the break belongs
4. Run it: `python3 escapes.py`.
5. Check it from the repository root: `./check m04l06-06`.

## Expected output

```text
She said, "I'm in!"
That was line one.
A backslash prints as one character: \
```

## How to check

`./check m04l06-06` copies `starter/` into a scratch directory and runs `python3 escapes.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
