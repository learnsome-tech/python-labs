# m13l06-05 · isdigit, and two old friends

**Lesson:** [More String Methods](https://learnsome.tech/learn/python-course/m13l06) (lesson 13.6, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can test what a string starts with, ends with or is made of, and build up conditions from string methods such as startswith, endswith, replace and isdigit.

In the lesson: The is digit method is true when a nonempty string is made entirely of digits, which corresponds exactly to the strings that represent a whole number. One stray letter makes it False. The empty string is False too, which is a sensible answer and saves you a special case. But a minus sign is not a digit, so a negative number written as a string fails, and you have to slice the sign off first before you ask. Two methods you already know are worth keeping to hand here: count tells you how many times something appears, and find tells you where the first one is.

## Files

- [`starter/shell-isdigit-and-two-old-friends.py`](starter/shell-isdigit-and-two-old-friends.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l06/m13l06-05/starter`
2. Read `shell-isdigit-and-two-old-friends.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   '2397'.isdigit()
   '23a'.isdigit()
   ''.isdigit()
   '-123'.isdigit()
   '-123'[1:].isdigit()
   '3.14'.count('.')
   '3.14'.find('.')
   ```
4. Run it: `python3 -i < shell-isdigit-and-two-old-friends.py`.
5. Check it from the repository root: `./check m13l06-05`.

## Expected output

```text
True
False
False
False
True
1
1
```

## How to check

`./check m13l06-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-isdigit-and-two-old-friends.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
