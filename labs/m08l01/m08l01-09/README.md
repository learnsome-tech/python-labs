# m08l01-09 · The classic surprise

**Lesson:** [Floats, Division And Mixed Types](https://learnsome.tech/learn/python-course/m08l01) (lesson 8.1, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can predict whether an arithmetic expression produces an int or a float, explain why floating point results are approximations, and write code that never depends on two floats being exactly equal.

In the lesson: Now the demonstration everybody remembers. Point one plus point two, in the shell. Python answers point three, then fifteen zeros, then a four. Ask it for point three on its own and it prints a tidy point three, so the two look different but you might think that is only display. The third line asks Python whether they are equal, using the double equals sign, which is the test we meet properly in chapter three. The answer is False. The stored approximation of point one plus point two is genuinely not the stored approximation of point three. The last line shows the fix: subtract, take the absolute value, and ask whether the gap is smaller than some tiny number you choose. Close enough, rather than equal, is the honest question.

## Files

- [`starter/shell-the-classic-surprise.py`](starter/shell-the-classic-surprise.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l01/m08l01-09/starter`
2. Read `shell-the-classic-surprise.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   0.1 + 0.2
   0.3
   0.1 + 0.2 == 0.3
   abs(0.1 + 0.2 - 0.3) < 1e-9
   ```
4. Run it: `python3 -i < shell-the-classic-surprise.py`.
5. Check it from the repository root: `./check m08l01-09`.

## Expected output

```text
0.30000000000000004
0.3
False
True
```

## How to check

`./check m08l01-09` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-classic-surprise.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
