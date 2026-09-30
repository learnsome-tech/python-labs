# m13l05-02 · A short program that uses it

**Lesson:** [Compound Boolean Expressions](https://learnsome.tech/learn/python-course/m13l05) (lesson 13.5, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can build conditions with and, or and not, read their precedence and short circuit behaviour, and return a Boolean expression directly instead of wrapping it in an if else.

In the lesson: Here is a short program built round that compound condition. It reads the two numbers and converts them with the float function, then makes a single if else decision. Run it with one hundred and thirty credits and an average of three point two. Both parts of the condition are true, so the student is eligible. Change either number so its part fails and the else block runs instead. There is only one test in the program, even though the rule has two requirements.

## Files

- [`starter/graduateGPA.py`](starter/graduateGPA.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l05/m13l05-02/starter`
2. Read `graduateGPA.py`.
3. Run it: `python3 graduateGPA.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m13l05-02`.

## Expected output

```text
How many units of credit do you have? What is your GPA? You are eligible to graduate!
```

## How to check

`./check m13l05-02` copies `starter/` into a scratch directory and runs `python3 graduateGPA.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
