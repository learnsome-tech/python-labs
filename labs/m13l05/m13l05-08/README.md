# m13l05-08 · Chained comparisons, and why one is not enough

**Lesson:** [Compound Boolean Expressions](https://learnsome.tech/learn/python-course/m13l05) (lesson 13.5, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can build conditions with and, or and not, read their precedence and short circuit behaviour, and return a Boolean expression directly instead of wrapping it in an if else.

In the lesson: Python lets you chain comparisons, so you can write a value between two ends almost as you would in mathematics. Tempting, but here is the trap. The only requirement on the two corners of a rectangle is that they are diagonally opposite, not that the second is larger. Let the first corner be two hundred and the second one hundred, with a value plainly between them. The obvious test comes out False, and you can see why with the numbers filled in. Turning the ends the other way round gives True. Joining the two possibilities with or covers both cases. The last line shows a chain spelled out with and, which is what other languages make you write.

## Files

- [`starter/shell-chained-comparisons-and-why-one-is-not-enoug.py`](starter/shell-chained-comparisons-and-why-one-is-not-enoug.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l05/m13l05-08/starter`
2. Read `shell-chained-comparisons-and-why-one-is-not-enoug.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   end1 = 200
   end2 = 100
   val = 120
   end1 <= val <= end2
   200 <= 120 <= 100
   end2 <= val <= end1
   end1 <= val <= end2 or end2 <= val <= end1
   end1 <= val and val <= end2
   ```
4. Run it: `python3 -i < shell-chained-comparisons-and-why-one-is-not-enoug.py`.
5. Check it from the repository root: `./check m13l05-08`.

## Expected output

```text
False
False
True
True
False
```

## How to check

`./check m13l05-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-chained-comparisons-and-why-one-is-not-enoug.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
