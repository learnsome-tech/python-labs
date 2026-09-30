# m19l04-04 · Writing a generator with yield

**Lesson:** [Iterators And Generators](https://learnsome.tech/learn/python-course/m19l04) (lesson 19.4, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can explain what a for loop does in terms of iter and next, write a generator function with yield, and say why a generator costs no memory however long its sequence is.

In the lesson: Now write your own. This looks like an ordinary function, but one word is different: yield instead of return. That one word changes everything. Return hands a value back and ends the call. Yield hands a value out and pauses right here, keeping every local variable exactly as it was, and the next call to next carries on from that line. And calling the function runs none of the body at all; it returns a generator, ready and waiting. Run it and read the four results. You can loop over it directly, hand it to list to collect all of the values, or hand it to sum, which adds a hundred numbers that never existed together at any one moment.

## Files

- [`starter/countdown.py`](starter/countdown.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l04/m19l04-04/starter`
2. Read `countdown.py` the way the lesson builds it:
   - Lines 1–6: one word is different
   - Lines 7–12: loop over it directly
3. Notes from the lesson:
   - Line 5: hands a value out and pauses right here
   - Line 3: calling it runs none of the body; it returns a generator
4. Run it: `python3 countdown.py`.
5. Check it from the repository root: `./check m19l04-04`.

## Expected output

```text
3
2
1
[5, 4, 3, 2, 1]
5050
```

## How to check

`./check m19l04-04` copies `starter/` into a scratch directory and runs `python3 countdown.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
