# m07l07-08 · sep and end in the shell

**Lesson:** [The Print Function Keyword End](https://learnsome.tech/learn/python-course/m07l07) (lesson 7.7, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can use the print function's end keyword parameter, alone or together with sep, to print several things on one line from inside a loop and still finish the line properly.

In the lesson: A quick tour of the two keywords together. The first entry shows the default separator, a single space, between the three values. The second sets sep to a hyphen, so the hyphen goes between them instead. The third leaves sep alone and sets end to an exclamation mark, which replaces the newline. The fourth uses both keywords together, and you get the hyphens between and the exclamation mark at the end. The fifth is the same entry with the two keywords in the other order, and the result is identical, because keyword parameters are matched by name rather than by position. Swap their order as you please, but keep them after all the values.

## Files

- [`starter/shell-sep-and-end-in-the-shell.py`](starter/shell-sep-and-end-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l07/m07l07-08/starter`
2. Read `shell-sep-and-end-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   print('a', 'b', 'c')
   print('a', 'b', 'c', sep='-')
   print('a', 'b', end='!')
   print('a', 'b', sep='-', end='!')
   print('a', 'b', end='!', sep='-')
   ```
4. Run it: `python3 -i < shell-sep-and-end-in-the-shell.py`.
5. Check it from the repository root: `./check m07l07-08`.

## Expected output

```text
a b c
a-b-c
a b!
a-b!
a-b!
```

## How to check

`./check m07l07-08` copies `starter/` into a scratch directory and runs `python3 -i < shell-sep-and-end-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
