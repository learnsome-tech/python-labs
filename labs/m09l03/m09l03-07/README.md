# m09l03-07 · Finding inside Mississippi

**Lesson:** [String Slices](https://learnsome.tech/learn/python-course/m09l03) (lesson 9.3, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can take a slice of a string or list with either bound omitted or negative, predict its length, use find to locate a substring, and drive indices and slices from a loop variable.

In the lesson: Check that each of these makes sense; the comment line is there only to help you count. The first letter i in Mississippi sits at index one, not zero, because the capital M comes first. The substring s followed by i first appears at index three. The substring s followed by a is nowhere in the word, so we get minus one. And the last line searches for s followed by i again, but from index four, stepping over the first occurrence and reporting the next one, at index six.

## Files

- [`starter/shell-finding-inside-mississippi.py`](starter/shell-finding-inside-mississippi.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l03/m09l03-07/starter`
2. Read `shell-finding-inside-mississippi.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   #    01234567890
   s = 'Mississippi'
   s.find('i')
   s.find('si')
   s.find('sa')
   s.find('si', 4)
   ```
4. Run it: `python3 -i < shell-finding-inside-mississippi.py`.
5. Check it from the repository root: `./check m09l03-07`.

## Expected output

```text
1
3
-1
6
```

## How to check

`./check m09l03-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-finding-inside-mississippi.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
