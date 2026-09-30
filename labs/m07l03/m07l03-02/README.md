# m07l03-02 · Updating variables: updateVar.py

**Lesson:** [Lists, Range And The For Loop](https://learnsome.tech/learn/python-course/m07l03) (lesson 7.3, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can update a variable, write a list, generate a sequence with range, and read or write a basic for loop that walks over a list.

In the lesson: Other than in early shell examples, we have not yet changed the value of an existing variable. Here is a simple example, chosen as an illustration, in the file updateVar. Can you predict the result? The first line gives x the value three. The second gives y the value of x plus two, using the value x has when that line starts. The third line doubles y, reading the old y on the right and writing the new y on the left. The fourth changes x using the latest value of y. The last line prints both, and the answer is seven and ten.

## Files

- [`starter/updateVar.py`](starter/updateVar.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-02/starter`
2. Read `updateVar.py` the way the lesson builds it:
   - Lines 1–2: The first line gives x the value three
   - Lines 3: The third line doubles y
   - Lines 4–5: the last line prints both
3. Run it: `python3 updateVar.py`.
4. Check it from the repository root: `./check m07l03-02`.

## Expected output

```text
7 10
```

## How to check

`./check m07l03-02` copies `starter/` into a scratch directory and runs `python3 updateVar.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
