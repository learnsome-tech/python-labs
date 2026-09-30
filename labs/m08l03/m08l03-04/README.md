# m08l03-04 · Operators and precedence

**Lesson:** [Chapter One In One Sitting](https://learnsome.tech/learn/python-course/m08l03) (lesson 8.3, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can recall, in one sitting, every idea from chapter one: the types and their literals, variables, operators and precedence, strings and formatting, input and output, functions, dictionaries, loops and floats.

In the lesson: Group three: the arithmetic operators, in precedence order, highest first. Two stars for exponentiation, then multiply, divide, floor divide and remainder, then add and subtract. So times comes before plus, and parentheses override the lot. Exponentiation is highest of all and groups from the right, which is why the third line gives five hundred and twelve. Then three ways to divide fourteen by four. The single slash gives a float, three point five, always. The double slash is integer division, throwing away any remainder. And the percent sign gives just the remainder, two. The last line is a classic trap: the power binds tighter than the minus sign in front of it.

## Files

- [`starter/shell-operators-and-precedence.py`](starter/shell-operators-and-precedence.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-04/starter`
2. Read `shell-operators-and-precedence.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   2 + 3 * 4
   (2 + 3) * 4
   2**3**2
   14 / 4
   14 // 4
   14 % 4
   -3**2
   ```
4. Run it: `python3 -i < shell-operators-and-precedence.py`.
5. Check it from the repository root: `./check m08l03-04`.

## Expected output

```text
14
20
512
3.5
3
2
-9
```

## How to check

`./check m08l03-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-operators-and-precedence.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
