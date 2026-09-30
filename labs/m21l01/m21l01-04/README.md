# m21l01-04 · All at once, or one line at a time

**Lesson:** [Paths And Files The Modern Way](https://learnsome.tech/learn/python-course/m21l01) (lesson 21.1, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can open every file with a with statement, read it whole or line by line, append to it, choose an encoding on purpose, and build paths with pathlib that work on any operating system.

In the lesson: There are two ways to read a file and you should choose between them on purpose. The read method gives you the entire contents as one string, which is fine for a shopping list and terrible for a log file of several gigabytes, because the whole thing has to fit in memory at once. The second half of this program shows the alternative. A file object is iterable: loop over it directly and you get one line at a time, each ending in a newline character, and only one line is ever in memory. Here the enumerate function numbers them as they go, and the strip method removes the trailing newline before printing. Prefer the loop unless you have a reason not to.

## Files

- [`starter/lineByLine.py`](starter/lineByLine.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l01/m21l01-04/starter`
2. Read `lineByLine.py`.
3. Run it: `python3 lineByLine.py`.
4. Check it from the repository root: `./check m21l01-04`.

## Expected output

```text
18 3
1 bread
2 milk
3 apples
```

## How to check

`./check m21l01-04` copies `starter/` into a scratch directory and runs `python3 lineByLine.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
