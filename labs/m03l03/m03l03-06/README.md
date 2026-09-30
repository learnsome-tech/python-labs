# m03l03-06 · Converting between numbers and text

**Lesson:** [Types And Functions, A Whirlwind Tour](https://learnsome.tech/learn/python-course/m03l03) (lesson 3.3, module 3: Meet Idle And The Shell) · Pro  
**Check:** Graded

## Goal

You can name four kinds of Python data, call a function with none, one or several parameters, ask type and len about a value, convert between numbers and strings, and re-enter an earlier shell line in Idle.

In the lesson: Some of the names of types serve as conversion functions, where there is an obvious meaning for the conversion. Try each of these one at a time in the shell. The first uses the name of a type as a conversion: it takes the number twenty three and hands back a string of two characters. The second goes the other way round, taking a string of three digit characters and handing back the number one hundred and twenty five. Now note the presence and absence of quotes in the two answers. The first result is shown inside quotes because it is a string; the second is shown bare because it is a number. That tiny difference on screen is your evidence that the conversion really happened, and it is worth checking every time.

## Files

- [`starter/shell-converting-between-numbers-and-text.py`](starter/shell-converting-between-numbers-and-text.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-06/starter`
2. Read `shell-converting-between-numbers-and-text.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   str(23)
   int('125')
   ```
4. Run it: `python3 -i < shell-converting-between-numbers-and-text.py`.
5. Check it from the repository root: `./check m03l03-06`.

## Expected output

```text
'23'
125
```

## How to check

`./check m03l03-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-converting-between-numbers-and-text.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
