# m06l02-07 · Indentation decides what is remembered

**Lesson:** [Several Functions, And Flow Of Control](https://learnsome.tech/learn/python-course/m06l02) (lesson 6.2, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can put several function definitions in one file, predict the order in which the lines are executed, and see how indentation decides what is remembered and what is run.

In the lesson: Here is a small example that puts all the weight on one detail: whether a line is indented. Guess what the example file order dot py does, and then run it to check. The function f has two print calls in its body, both indented. Nothing is printed while the definition is read. The last line calls f, and only then do both lines appear, in the order they are written inside the body. So the question the second print call asks is answered: it prints when f is invoked, at the end of the program, not on the way past.

## Files

- [`starter/order.py`](starter/order.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-07/starter`
2. Read `order.py`.
3. Notes from the lesson:
   - Line 3: indented, so it belongs to the function
4. Run it: `python3 order.py`.
5. Check it from the repository root: `./check m06l02-07`.

## Expected output

```text
In function f
When does this print?
```

## How to check

`./check m06l02-07` copies `starter/` into a scratch directory and runs `python3 order.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
