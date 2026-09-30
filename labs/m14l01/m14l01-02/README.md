# m14l01-02 · cool.py, the tea made numerical

**Lesson:** [While Loops, And The General Range](https://learnsome.tech/learn/python-course/m14l01) (lesson 14.1, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop whose condition is tested before every pass, spot a loop that will never stop, and use the three argument range function to replace a counting while loop with a for loop.

In the lesson: Let us make that concrete. The tea starts at one hundred and fifteen degrees Fahrenheit, you want it at one hundred and twelve, and one chip of ice lowers the temperature by one degree. The loop prints the temperature first and then reduces it. Each time execution reaches the end of the indented block it returns to the heading again for another test, and when the test is finally false it jumps past the indented body to the next statement in sequence. I added the last line after the loop to remind you of that. Run it and three temperatures are printed, then the message that the tea is cool enough.

## Files

- [`starter/cool.py`](starter/cool.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l01/m14l01-02/starter`
2. Read `cool.py` the way the lesson builds it:
   - Lines 1: starts at one hundred and fifteen
   - Lines 2–4: prints the temperature first
   - Lines 5–6: after the loop
3. Notes from the lesson:
   - Line 2: tested before every pass through the two indented lines
4. Run it: `python3 cool.py`.
5. Check it from the repository root: `./check m14l01-02`.

## Expected output

```text
115
114
113
The tea is cool enough.
```

## How to check

`./check m14l01-02` copies `starter/` into a scratch directory and runs `python3 cool.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
