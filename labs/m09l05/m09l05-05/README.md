# m09l05-05 · The example program multiply1.py

**Lesson:** [Appending To Lists, Sets, Constructors](https://learnsome.tech/learn/python-course/m09l05) (lesson 9.5, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can grow a list with append inside a loop, explain why that differs from concatenation, build a set to remove duplicates, and recognise a type name used as a constructor.

In the lesson: Test yourself before you read the body: if we are going to accumulate a list, how do we initialise it? With an empty list, just as we started an accumulating total at zero. In earlier accumulation loops we needed an assignment statement to change the object doing the accumulating, but now the method append modifies its list for us, so there is no assignment statement inside the loop. The loop runs num over the given list and appends the product of num and the multiplier each time. Then the function returns the finished list, and the last line prints the result of calling it. Run it and the answer is the three products in the original order.

## Files

- [`starter/multiply1.py`](starter/multiply1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l05/m09l05-05/starter`
2. Read `multiply1.py` the way the lesson builds it:
   - Lines 1–10: an empty list
   - Lines 11–12: appends the product
   - Lines 13–15: returns the finished list
3. Notes from the lesson:
   - Line 10: how we initialise an accumulation of a list: an empty one
   - Line 12: no assignment needed: append modifies newList itself
4. Run it: `python3 multiply1.py`.
5. Check it from the repository root: `./check m09l05-05`.

## Expected output

```text
[15, 5, 35]
```

## How to check

`./check m09l05-05` copies `starter/` into a scratch directory and runs `python3 multiply1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
