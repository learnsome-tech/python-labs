# m07l03-06 · A first for loop

**Lesson:** [Lists, Range And The For Loop](https://learnsome.tech/learn/python-course/m07l03) (lesson 7.3, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can update a variable, write a list, generate a sequence with range, and read or write a basic for loop that walks over a list.

In the lesson: The tutorial has you type this into the shell, where you get continuation lines and must enter one empty line to finish. In a file it is easier to see whole. This is a for loop. It has a heading starting with the word for, followed by a variable name, count here, then the word in, then a sequence, then a final colon. As with function definitions, the colon says that a consistently indented block follows. The block is repeated once for each element, so these two lines run three times, and the loop variable takes the next value each pass: one, then two, and finally three.

## Files

- [`starter/firstloop.py`](starter/firstloop.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-06/starter`
2. Read `firstloop.py` the way the lesson builds it:
   - Lines 1: a heading starting with the word for
   - Lines 2–3: a consistently indented block
3. Run it: `python3 firstloop.py`.
4. Check it from the repository root: `./check m07l03-06`.

## Expected output

```text
1
Yes
2
YesYes
3
YesYesYes
```

## How to check

`./check m07l03-06` copies `starter/` into a scratch directory and runs `python3 firstloop.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
