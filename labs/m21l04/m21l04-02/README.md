# m21l04-02 · math and statistics: the numbers you were taught

**Lesson:** [A Standard Library Tour](https://learnsome.tech/learn/python-course/m21l04) (lesson 21.4, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can name the standard library modules a beginner actually meets, say what each one is for, recognise when a problem belongs to one of them, and look the details up for yourself.

In the lesson: First, arithmetic beyond the operators. The math module has square root, pi, rounding down and up, factorials, logarithms and the trigonometry functions. One member deserves a spotlight: is close, on the third line of output. You met the floating point problem earlier in the course, where nought point one plus nought point two is not quite nought point three; is close is the honest way to ask whether two floats are near enough, and it is what you should use instead of the equals equals comparison. Alongside it, statistics gives you mean, median, mode and standard deviation without a single loop of your own. If you find yourself adding a list up and dividing by its length, this module already did it.

## Files

- [`starter/mathStats.py`](starter/mathStats.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l04/m21l04-02/starter`
2. Read `mathStats.py`.
3. Notes from the lesson:
   - Line 6: the honest way to compare two floats
4. Run it: `python3 mathStats.py`.
5. Check it from the repository root: `./check m21l04-02`.

## Expected output

```text
1.4142135623730951 3.141592653589793
3 4 120
True
71.4
72 72
12.442
```

## How to check

`./check m21l04-02` copies `starter/` into a scratch directory and runs `python3 mathStats.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
