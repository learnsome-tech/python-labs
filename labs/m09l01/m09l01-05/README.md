# m09l01-05 · Counting substrings with count

**Lesson:** [Objects, Methods And String Case](https://learnsome.tech/learn/python-course/m09l01) (lesson 9.1, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can call a method on a string with the object dot method syntax, explain why a string method returns a new string instead of changing the original, and use upper, lower, capitalize, title and count.

In the lesson: The first method we meet that takes a parameter is count. Given a string s and a substring sub, count returns the number of repetitions of sub that appear as substrings inside s. Read each line and make sure you agree with the answer. There are three letter i's in the sentence. There are two occurrences of the substring i followed by s. There are no occurrences of the word That with a capital T, so the answer is zero. And the last line has a blank between the quotes: there are five blanks in the sentence. Blanks are characters like any other, except that you cannot see them, and count is perfectly happy to count them.

## Files

- [`starter/shell-counting-substrings-with-count.py`](starter/shell-counting-substrings-with-count.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l01/m09l01-05/starter`
2. Read `shell-counting-substrings-with-count.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   tale = 'This is the best of times.'
   tale.count('i')
   tale.count('is')
   tale.count('That')
   tale.count(' ')
   ```
4. Run it: `python3 -i < shell-counting-substrings-with-count.py`.
5. Check it from the repository root: `./check m09l01-05`.

## Expected output

```text
3
2
0
5
```

## How to check

`./check m09l01-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-counting-substrings-with-count.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
