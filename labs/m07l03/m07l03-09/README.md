# m07l03-09 · for123a.py: one line indented, everything changes

**Lesson:** [Lists, Range And The For Loop](https://learnsome.tech/learn/python-course/m07l03) (lesson 7.3, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can update a variable, write a list, generate a sequence with range, and read or write a basic for loop that walks over a list.

In the lesson: As with the indented block in a function, it is important to get the indentation right. Alter the code so the fourth line is indented, and change nothing else. Predict the change, then run it. Because that print now sits inside the loop body, it runs on every pass, so Done counting appears three times over, interleaved with the counting, and the message has become a lie. The colour loop at the bottom is untouched. Four spaces changed the meaning of the program without changing a word of it.

## Files

- [`starter/for123a.py`](starter/for123a.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-09/starter`
2. Read `for123a.py` the way the lesson builds it:
   - Lines 1–4: the fourth line is indented
   - Lines 5–6: The colour loop at the bottom
3. Run it: `python3 for123a.py`.
4. Check it from the repository root: `./check m07l03-09`.

## Expected output

```text
1
Yes
Done counting.
2
YesYes
Done counting.
3
YesYesYes
Done counting.
red
blue
green
```

## How to check

`./check m07l03-09` copies `starter/` into a scratch directory and runs `python3 for123a.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
