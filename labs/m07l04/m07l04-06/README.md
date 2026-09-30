# m07l04-06 · Start with the part that is easy

**Lesson:** [Repeat Loops And Successive Modification](https://learnsome.tech/learn/python-course/m07l04) (lesson 7.4, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can write a simple repeat loop whose loop variable you never use, and build a loop that modifies a variable of your own on every pass, tracing its value pass by pass.

In the lesson: First, allow yourself to omit the numbers. Then the work for any one element is a single line: print the item. Wrap that in a for each loop over items and the job is finished. Run it and the four colour names come out on four lines. This is worth doing even though it is not the answer yet. It settles the sequence and the loop heading, so from here on I can think about one element at a time, with the name I chose in the heading, and worry only about the number in front.

## Files

- [`starter/items.py`](starter/items.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-06/starter`
2. Read `items.py`.
3. Run it: `python3 items.py`.
4. Check it from the repository root: `./check m07l04-06`.

## Expected output

```text
red
orange
yellow
green
```

## How to check

`./check m07l04-06` copies `starter/` into a scratch directory and runs `python3 items.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
