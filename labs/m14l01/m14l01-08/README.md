# m14l01-08 · The counting while becomes a for

**Lesson:** [While Loops, And The General Range](https://learnsome.tech/learn/python-course/m14l01) (lesson 14.1, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop whose condition is tested before every pass, spot a loop that will never stop, and use the three argument range function to replace a counting while loop with a for loop.

In the lesson: Here is the point of the three argument range. The earlier while loops were chosen for their simplicity, and any of them could have been rewritten with a range call. The first line builds the same list in one go, and printing it gives the square bracketed list the earlier program worked so hard for. The loop underneath prints the numbers one at a time, and it does the work of the whole earlier program: no counter to initialise, no test to write, no line at the bottom to increase i, because the range and the for heading handle all three. Run it and both forms agree. The conversion runs backwards too. Any for loop over a range can be rewritten as a while loop: set the variable before the loop, test it in the heading, and change it as the last action of the body. That is the pattern to fall back on when the sequence is not a plain arithmetic count.

## Files

- [`starter/testWhileAsFor.py`](starter/testWhileAsFor.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l01/m14l01-08/starter`
2. Read `testWhileAsFor.py`.
3. Run it: `python3 testWhileAsFor.py`.
4. Check it from the repository root: `./check m14l01-08`.

## Expected output

```text
[4, 6, 8]
4
6
8
```

## How to check

`./check m14l01-08` copies `starter/` into a scratch directory and runs `python3 testWhileAsFor.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
