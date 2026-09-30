# m06l05-07 · One function, one job

**Lesson:** [Returning Values](https://learnsome.tech/learn/python-course/m06l05) (lesson 6.5, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function that returns a value, use a call inside a larger expression, and tell the difference between a function that prints and a function that returns.

In the lesson: Compare return two with addition five from the previous module. Both use functions, and both print, but where the printing is done differs. The function sumProblem prints directly inside the function and returns nothing explicitly, so the caller gets to decide nothing. In general, a function should do a single thing, because then you have more flexibility in combining functions. The old sumProblem did two things: it created a sentence and it printed it. If that is all you have, you are out of luck when you want the sentence for something else. A better way is a function that creates the sentence and returns it for whatever further use you want. Printing is one possibility, and that is addition six. Run addition six: the output is the same, and the design is better.

## Files

- [`starter/addition6.py`](starter/addition6.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-07/starter`
2. Read `addition6.py`.
3. Notes from the lesson:
   - Line 7: builds the sentence and hands it back
   - Line 10: the caller decides to print it
4. Run it: `python3 addition6.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m06l05-07`.

## Expected output

```text
The sum of 2 and 3 is 5.
The sum of 1234567890123 and 535790269358 is 1770358159481.
Enter an integer: Enter another integer: The sum of 8 and 5 is 13.
```

## How to check

`./check m06l05-07` copies `starter/` into a scratch directory and runs `python3 addition6.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
