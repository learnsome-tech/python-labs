# m14l01-05 · testWhile2.py, the order matters

**Lesson:** [While Loops, And The General Range](https://learnsome.tech/learn/python-course/m14l01) (lesson 14.1, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop whose condition is tested before every pass, spot a loop that will never stop, and use the three argument range function to replace a counting while loop with a for loop.

In the lesson: Predict what happens with this slight variation, which only swaps the order of the two statements in the body. Follow it carefully, one step at a time. Because i is increased before it is printed, the first number printed is six, not four. The second surprise is at the end. Many people assume ten will not be printed, since ten is past nine, but the test that stops the loop is made only when the loop starts again, and no test is made in the middle of the loop. Once the body has started it runs to the end, even when i has become ten. Run it and the answer is six, eight, ten. In Python, while is not used quite as in English, where you might mean to stop the moment the condition fails.

## Files

- [`starter/testWhile2.py`](starter/testWhile2.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l01/m14l01-05/starter`
2. Read `testWhile2.py`.
3. Notes from the lesson:
   - Line 3: no test happens here, in the middle of the body
4. Run it: `python3 testWhile2.py`.
5. Check it from the repository root: `./check m14l01-05`.

## Expected output

```text
6
8
10
```

## How to check

`./check m14l01-05` copies `starter/` into a scratch directory and runs `python3 testWhile2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
