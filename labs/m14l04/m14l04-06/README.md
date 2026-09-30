# m14l04-06 · A condition that looks right and is wrong

**Lesson:** [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) (lesson 14.4, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can say which values of any type Python treats as False, use the Pythonic test for an empty collection, and recognise the bugs that arise when a comparison and an or are combined carelessly.

In the lesson: This automatic conversion can also lead to extra trouble. Suppose you prompt the user for the answer to a yes or no question, and you want to accept the letter y or the word yes as meaning True. You might well write the condition on the second line here. It reads like English, but it does not mean what it appears to say. Run it. The first time, the answer is the letter y and the message prints, which looks correct. The second time, the answer is the word no, and the message prints again, which is plainly wrong. Python detects no error at all.

## Files

- [`starter/boolConfusion.py`](starter/boolConfusion.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l04/m14l04-06/starter`
2. Read `boolConfusion.py`.
3. Run it: `python3 boolConfusion.py`.
4. Check it from the repository root: `./check m14l04-06`.

## Expected output

```text
y is OK
no is OK!!???
```

## How to check

`./check m14l04-06` copies `starter/` into a scratch directory and runs `python3 boolConfusion.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
