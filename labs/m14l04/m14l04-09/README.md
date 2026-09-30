# m14l04-09 · What or and and actually hand back

**Lesson:** [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) (lesson 14.4, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can say which values of any type Python treats as False, use the Pythonic test for an empty collection, and recognise the bugs that arise when a comparison and an or are combined carelessly.

In the lesson: Things get even stranger. Enter these six conditions themselves, one at a time, directly into the shell, and watch what comes back. The first gives True, as you would expect. The second gives the string yes, which is not a Boolean at all. The third gives that string as well, and the fourth gives False. Then, with two plain strings as operands, or hands back the first and and hands back the second. Every one of these would still steer an if statement correctly, because each result converts to the right Boolean. The values themselves, though, are not Booleans.

## Files

- [`starter/shell-what-or-and-and-actually-hand-back.py`](starter/shell-what-or-and-and-actually-hand-back.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l04/m14l04-09/starter`
2. Read `shell-what-or-and-and-actually-hand-back.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   'y' == 'y' or 'yes'
   'no' == 'y' or 'yes'
   'y' == 'y' and 'yes'
   'no' == 'y' and 'yes'
   'no' or 'yes'
   'no' and 'yes'
   ```
4. Run it: `python3 -i < shell-what-or-and-and-actually-hand-back.py`.
5. Check it from the repository root: `./check m14l04-09`.

## Expected output

```text
True
'yes'
'yes'
False
'no'
'yes'
```

## How to check

`./check m14l04-09` copies `starter/` into a scratch directory and runs `python3 -i < shell-what-or-and-and-actually-hand-back.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
