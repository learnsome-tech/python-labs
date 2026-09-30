# m07l04-02 · The simple repeat loop

**Lesson:** [Repeat Loops And Successive Modification](https://learnsome.tech/learn/python-course/m07l04) (lesson 7.4, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can write a simple repeat loop whose loop variable you never use, and build a loop that modifies a variable of your own on every pass, tracing its value pass by pass.

In the lesson: Read and run the example program repeat one. It opens with a documentation string, then the loop heading asks the range function for ten values, and the body prints the string Hello. Run it and you get ten lines of Hello. Now look closely at the heading. The variable i is introduced there only because a for loop must name a variable, and the body never mentions it. Nothing the body does depends on which pass we are on. That is the point of a simple repeat loop: the number of values matters, and what they are does not.

## Files

- [`starter/repeat1.py`](starter/repeat1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-02/starter`
2. Read `repeat1.py` the way the lesson builds it:
   - Lines 1: a documentation string
   - Lines 2–3: the range function
   - Lines 4: the body prints
3. Run it: `python3 repeat1.py`.
4. Check it from the repository root: `./check m07l04-02`.

## Expected output

```text
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
```

## How to check

`./check m07l04-02` copies `starter/` into a scratch directory and runs `python3 repeat1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
