# m07l03-11 · types1.py, five lines that beg for a loop

**Lesson:** [Lists, Range And The For Loop](https://learnsome.tech/learn/python-course/m07l03) (lesson 7.3, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can update a variable, write a list, generate a sequence with range, and read or write a basic for loop that walks over a list.

In the lesson: Before the exercises, look at this small program, types one. It prints five values, each with the type of that value: an integer, a float, an empty list, a boolean, and the None object. Every line says the same sort of thing about a different value, so this is the for each pattern waiting to happen. Run it and keep the output in front of you.

## Files

- [`starter/types1.py`](starter/types1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-11/starter`
2. Read `types1.py`.
3. Run it: `python3 types1.py`.
4. Check it from the repository root: `./check m07l03-11`.

## Expected output

```text
2 <class 'int'>
3.5 <class 'float'>
[] <class 'list'>
True <class 'bool'>
None <class 'NoneType'>
```

## How to check

`./check m07l03-11` copies `starter/` into a scratch directory and runs `python3 types1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
