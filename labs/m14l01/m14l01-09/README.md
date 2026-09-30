# m14l01-09 · Counting down to blastoff

**Lesson:** [While Loops, And The General Range](https://learnsome.tech/learn/python-course/m14l01) (lesson 14.1, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can write a while loop whose condition is tested before every pass, spot a loop that will never stop, and use the three argument range function to replace a counting while loop with a for loop.

In the lesson: These ranges, like the simpler ones we used earlier, are most often used as the sequence in a for loop heading. Here the count runs from ten down to one, with a step of minus one, and then a line after the loop announces blastoff. Run it. Ten numbers appear in descending order, and one is the last of them, because the second argument, zero, is past the end. Getting that boundary right is the one thing to watch with a negative step: think of the second value as the first number you do not want.

## Files

- [`starter/countdown.py`](starter/countdown.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l01/m14l01-09/starter`
2. Read `countdown.py`.
3. Run it: `python3 countdown.py`.
4. Check it from the repository root: `./check m14l01-09`.

## Expected output

```text
10
9
8
7
6
5
4
3
2
1
Blastoff!
```

## How to check

`./check m14l01-09` copies `starter/` into a scratch directory and runs `python3 countdown.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
