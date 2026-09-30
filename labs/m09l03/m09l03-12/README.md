# m09l03-12 · The example program index1.py

**Lesson:** [String Slices](https://learnsome.tech/learn/python-course/m09l03) (lesson 9.3, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

In the lesson: Here is the example program index one dot py. It sets a string, prints it whole, then computes n as the length. The for loop runs i over range n, so i takes every valid index in turn. Inside the loop the first print with no arguments leaves a blank line between the groups. Then we print i, the character at index i, the slice of everything before index i, and the slice of everything before index i plus two. Run it and read the output against the code. When i is zero the part before index zero is empty, which is why that line looks bare. And once i reaches two, the slice has run past the end, and the forgiving rule gives the whole word.

## Files

- [`starter/index1.py`](starter/index1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l03/m09l03-12/starter`
2. Read `index1.py` the way the lesson builds it:
   - Lines 1–5: computes n as the length
   - Lines 6–8: leaves a blank line
   - Lines 9–11: the slice of everything before
3. Notes from the lesson:
   - Line 6: i takes every valid index of s, zero through n - 1
   - Line 11: i+2 may run past the end; a slice tolerates that
4. Run it: `python3 index1.py`.
5. Check it from the repository root: `./check m09l03-12`.

## Expected output

```text
The full string is:  word

i = 0
The letter at index i: w
The part before index i (if any):
The part before index i+2: wo

i = 1
The letter at index i: o
The part before index i (if any): w
The part before index i+2: wor

i = 2
The letter at index i: r
The part before index i (if any): wo
The part before index i+2: word

i = 3
The letter at index i: d
The part before index i (if any): wor
The part before index i+2: word
```

## How to check

`./check m09l03-12` copies `starter/` into a scratch directory and runs `python3 index1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
