# m06l04-02 · Two parameters, three calls

**Lesson:** [Multiple Parameters](https://learnsome.tech/learn/python-course/m06l04) (lesson 6.4, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can define and call a function with several parameters, and explain how the arguments are matched to the parameter names from left to right.

In the lesson: Here is addition five, a change to the earlier addition program that uses a function to make it easy to display many sum problems. Read and follow the code, and then run it. The function sumProblem has two formal parameters, x and y. Its body adds them, builds a sentence with the string format method, and prints it. Then main makes three calls. The first passes two small numbers. The second passes two numbers far too long to want to type twice. The third asks the user for two integers, converts them with the int function, and passes those. Three calls, three different pairs of values, one definition. The keyboard work stays in main, away from the arithmetic, so the function that does the sums never has to care where its numbers came from.

## Files

- [`starter/addition5.py`](starter/addition5.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-02/starter`
2. Read `addition5.py` the way the lesson builds it:
   - Lines 1–8: two formal parameters
   - Lines 9–15: three calls
   - Lines 16–17: one definition
3. Notes from the lesson:
   - Line 5: x and y are the formal parameters
   - Line 12: arguments can be as large as you like
4. Run it: `python3 addition5.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m06l04-02`.

## Expected output

```text
The sum of 2 and 3 is 5.
The sum of 1234567890123 and 535790269358 is 1770358159481.
Enter an integer: Enter another integer: The sum of 8 and 5 is 13.
```

## How to check

`./check m06l04-02` copies `starter/` into a scratch directory and runs `python3 addition5.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
