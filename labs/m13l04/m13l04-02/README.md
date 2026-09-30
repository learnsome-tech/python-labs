# m13l04-02 · onlyPositive dot py

**Lesson:** [Nesting Control Flow Statements](https://learnsome.tech/learn/python-course/m13l04) (lesson 13.4, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can nest if statements inside loops and loops inside if statements, and read the indentation to see which block belongs to which heading.

In the lesson: Here is the whole thing. The loop heading comes first, and the if sits inside the loop body. Read the indentation carefully, because it carries the meaning. The if line is indented under the for, so the test happens once for every element. The print is indented under the if, so it happens only when the test succeeds. The last line tests the function on a mixed list. Out come three, two and seven. This one idea widens what loops can do: different things at different times through a loop, given a consistent test.

## Files

- [`starter/onlyPositive.py`](starter/onlyPositive.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l04/m13l04-02/starter`
2. Read `onlyPositive.py` the way the lesson builds it:
   - Lines 1–5: the loop heading comes first
   - Lines 6–7: the if sits inside the loop body
   - Lines 8–9: the last line tests the function
3. Notes from the lesson:
   - Line 6: indented under for, so it runs once per element
   - Line 7: indented under if, so it runs only when the test is True
4. Run it: `python3 onlyPositive.py`.
5. Check it from the repository root: `./check m13l04-02`.

## Expected output

```text
3
2
7
```

## How to check

`./check m13l04-02` copies `starter/` into a scratch directory and runs `python3 onlyPositive.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
