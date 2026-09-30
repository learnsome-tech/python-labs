# m06l05-05 · Printing is not returning

**Lesson:** [Returning Values](https://learnsome.tech/learn/python-course/m06l05) (lesson 6.5, module 6: Functions) · Pro  
**Check:** Graded

## Goal

You can write a function that returns a value, use a call inside a larger expression, and tell the difference between a function that prints and a function that returns.

In the lesson: This is the confusion that costs beginners the most time, so here it is in the Shell. Two functions, one that prints its answer and one that returns it. Call each one on its own and both look identical, because the Shell shows a returned value as well as anything printed. Now print what each call gives back. The returning function gives back five. The printing function prints five and then gives back None, because a function that returns nothing explicitly still returns something. Finally, use the answer in a larger expression. The returning one multiplies happily by ten. The printing one cannot: you cannot multiply None. Printing sends text to the screen. Returning hands a value to whoever called you.

## Files

- [`starter/shell-printing-is-not-returning.py`](starter/shell-printing-is-not-returning.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-05/starter`
2. Read `shell-printing-is-not-returning.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   def printSum(x, y):
       print(x + y)
   def returnSum(x, y):
       return x + y
   printSum(2, 3)
   returnSum(2, 3)
   print(printSum(2, 3))
   print(returnSum(2, 3))
   returnSum(2, 3) * 10
   printSum(2, 3) * 10
   ```
4. Run it: `python3 -i < shell-printing-is-not-returning.py`.
5. Check it from the repository root: `./check m06l05-05`.

## Expected output

```text
5
5
5
None
5
50
5
Traceback (most recent call last):
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

## How to check

`./check m06l05-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-printing-is-not-returning.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
