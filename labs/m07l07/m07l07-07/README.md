# m07l07-07 · Finishing the line after the loop

**Lesson:** [The Print Function Keyword End](https://learnsome.tech/learn/python-course/m07l07) (lesson 7.7, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can use the print function's end keyword parameter, alone or together with sep, to print several things on one line from inside a loop and still finish the line properly.

In the lesson: The cure is one extra call to the print function, with no values at all, after the loop. It prints nothing and then adds the default newline, which finishes off the line the loop built. Look carefully at its indentation. It is lined up with the for heading, not with the loop body, so it runs once when the loop is over, and not on every pass. Now the fruit names share a line and the sentence has its own line. That pattern, suppress the newline in the body and add one afterwards, is the standard way to print a row of things from a loop.

## Files

- [`starter/endSpace2.py`](starter/endSpace2.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l07/m07l07-07/starter`
2. Read `endSpace2.py` the way the lesson builds it:
   - Lines 1–4: one extra call to the print function
   - Lines 5–7: the sentence has its own line
3. Notes from the lesson:
   - Line 4: indented with the for heading, so it runs once, after the loop
4. Run it: `python3 endSpace2.py`.
5. Check it from the repository root: `./check m07l07-07`.

## Expected output

```text
apple banana pear
This is probably better!
```

## How to check

`./check m07l07-07` copies `starter/` into a scratch directory and runs `python3 endSpace2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
