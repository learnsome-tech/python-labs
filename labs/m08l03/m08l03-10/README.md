# m08l03-10 · The four loop patterns

**Lesson:** [Chapter One In One Sitting](https://learnsome.tech/learn/python-course/m08l03) (lesson 8.3, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can recall, in one sitting, every idea from chapter one: the types and their literals, variables, operators and precedence, strings and formatting, input and output, functions, dictionaries, loops and floats.

In the lesson: Group eight: loops, and the patterns the summary names. The heading is the word for, a variable, the word in, a sequence, and a colon, then an indented block repeated once per element. The first block is an accumulation loop: initialise the total to hold none of the sequence, then combine one item at a time into it. The second is a for each loop over a list, doing the same sort of thing with every item. The third is a repeat loop counting how many times, where the underscore is the variable name only because a heading needs one; inside it count is successively modified, preparing the next value. Run all three and check the output against your prediction.

## Files

- [`starter/summaryLoops.py`](starter/summaryLoops.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-10/starter`
2. Read `summaryLoops.py` the way the lesson builds it:
   - Lines 1–4: an accumulation loop
   - Lines 5–8: a for each loop
   - Lines 9–14: the underscore
3. Run it: `python3 summaryLoops.py`.
4. Check it from the repository root: `./check m08l03-10`.

## Expected output

```text
sum: 10
red green
step 1; step 2; step 4;
```

## How to check

`./check m08l03-10` copies `starter/` into a scratch directory and runs `python3 summaryLoops.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
