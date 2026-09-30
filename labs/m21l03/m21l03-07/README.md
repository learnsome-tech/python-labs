# m21l03-07 · Shuffling, sampling and repeated choices

**Lesson:** [Dates, Times And Random](https://learnsome.tech/learn/python-course/m21l03) (lesson 21.3, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can make and compare dates, do arithmetic with timedelta, format and parse them with strftime and strptime, and generate random numbers you can reproduce with a seed.

In the lesson: Three more functions, and one distinction worth holding on to. Shuffle rearranges a list in place: it changes the list you give it and returns nothing, so never write deck is assigned the shuffle of deck. Sample draws several items with no repeats, which is what a lottery does, and here it draws six numbers from one to forty nine. Choices, with an s, does the opposite: it draws with replacement, so the same item can come up again, which is what tossing a coin does. Because the program seeds the generator first, the three answers on screen are what you will see too, which is the only reason I can print them at all.

## Files

- [`starter/randomLists.py`](starter/randomLists.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l03/m21l03-07/starter`
2. Read `randomLists.py`.
3. Run it: `python3 randomLists.py`.
4. Check it from the repository root: `./check m21l03-07`.

## Expected output

```text
['queen', 'king', 'jack', 'ace']
[16, 15, 9, 7, 44, 35]
['heads', 'heads', 'heads', 'heads', 'tails']
```

## How to check

`./check m21l03-07` copies `starter/` into a scratch directory and runs `python3 randomLists.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
