# m07l03-08 · for123.py: dedenting ends the block

**Lesson:** [Lists, Range And The For Loop](https://learnsome.tech/learn/python-course/m07l03) (lesson 7.3, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can update a variable, write a list, generate a sequence with range, and read or write a basic for loop that walks over a list.

In the lesson: Here is the same loop in a file, with more after it. In a file the blank line is not necessary, because the interpreter need not respond immediately. Instead, as with a function definition, you indicate being past the indented block by dedenting. The print of Done counting has the same level of indentation as the for heading, so the two run in sequence, and it is printed once, after the loop completes all of its repetitions. Execution ends with another simple loop, over colour names. Match every line of output to the code that produced it.

## Files

- [`starter/for123.py`](starter/for123.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-08/starter`
2. Read `for123.py` the way the lesson builds it:
   - Lines 1–3: the same loop in a file
   - Lines 4: the same level of indentation as the for heading
   - Lines 5–6: another simple loop
3. Run it: `python3 for123.py`.
4. Check it from the repository root: `./check m07l03-08`.

## Expected output

```text
1
Yes
2
YesYes
3
YesYesYes
Done counting.
red
blue
green
```

## How to check

`./check m07l03-08` copies `starter/` into a scratch directory and runs `python3 for123.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
