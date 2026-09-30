# m03l03-04 · How long is it

**Lesson:** [Types And Functions, A Whirlwind Tour](https://learnsome.tech/learn/python-course/m03l03) (lesson 3.3, module 3: Meet Idle And The Shell) · Pro  
**Check:** Graded

## Goal

You can name four kinds of Python data, call a function with none, one or several parameters, ask type and len about a value, convert between numbers and strings, and re-enter an earlier shell line in Idle.

In the lesson: Strings and lists are both sequences of parts: characters in the one case, elements in the other. We can find the length of that sequence with another function, with the abbreviated name len. Try both of the following separately in the shell. The list holds three elements, so the answer is three. The string holds four characters, so the answer is four. Notice that len does not care which of the two you hand it. That is a habit worth spotting early: a lot of Python is written so that one function works on anything that has the right shape, rather than one function per type. It is the reason the language stays small while doing a great deal.

## Files

- [`starter/shell-how-long-is-it.py`](starter/shell-how-long-is-it.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-04/starter`
2. Read `shell-how-long-is-it.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   len([2, 4, 6])
   len('abcd')
   ```
4. Run it: `python3 -i < shell-how-long-is-it.py`.
5. Check it from the repository root: `./check m03l03-04`.

## Expected output

```text
3
4
```

## How to check

`./check m03l03-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-how-long-is-it.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
