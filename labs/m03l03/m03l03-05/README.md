# m03l03-05 · No parameters, and several

**Lesson:** [Types And Functions, A Whirlwind Tour](https://learnsome.tech/learn/python-course/m03l03) (lesson 3.3, module 3: Meet Idle And The Shell) · Pro  
**Check:** Graded

## Goal

You can name four kinds of Python data, call a function with none, one or several parameters, ask type and len about a value, convert between numbers and strings, and re-enter an earlier shell line in Idle.

In the lesson: Some functions have no parameters, so nothing goes between the parentheses. For example, some types serve as no-parameter functions to create a simple value of their own type. Try the first line on screen. What comes back is an opening and a closing square bracket with nothing between them, which is the way an empty list is displayed. The parentheses are still required, even with nothing inside; that is what makes it a call. Functions may also take more than one parameter, separated by commas. Try the second line. Here max, which is short for maximum, is given three numbers and hands back the largest of them, eleven. One function, no parameters; another function, three. The shape of the call is the same either way.

## Files

- [`starter/shell-no-parameters-and-several.py`](starter/shell-no-parameters-and-several.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-05/starter`
2. Read `shell-no-parameters-and-several.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   list()
   max(5, 11, 2)
   ```
4. Run it: `python3 -i < shell-no-parameters-and-several.py`.
5. Check it from the repository root: `./check m03l03-05`.

## Expected output

```text
[]
11
```

## How to check

`./check m03l03-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-no-parameters-and-several.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
