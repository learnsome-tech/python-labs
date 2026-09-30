# m07l03-05 · The range function, part one

**Lesson:** [Lists, Range And The For Loop](https://learnsome.tech/learn/python-course/m07l03) (lesson 7.3, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can update a variable, write a list, generate a sequence with range, and read or write a basic for loop that walks over a list.

In the lesson: There is a built in function called range that generates regular arithmetic sequences automatically. Try these in the shell. The pattern is the word range, then in parentheses the size of the sequence you want. It generates the integers one at a time, as needed, which in the jargon is called lazy evaluation. To see all the results at once, convert to a list. The sequence starts at zero and ends before the parameter, so the number of elements is the number you asked for. Ask for the range on its own and it reports its start and stop.

## Files

- [`starter/shell-the-range-function-part-one.py`](starter/shell-the-range-function-part-one.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-05/starter`
2. Read `shell-the-range-function-part-one.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   list(range(4))
   list(range(10))
   range(4)
   ```
4. Run it: `python3 -i < shell-the-range-function-part-one.py`.
5. Check it from the repository root: `./check m07l03-05`.

## Expected output

```text
[0, 1, 2, 3]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(0, 4)
```

## How to check

`./check m07l03-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-range-function-part-one.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
