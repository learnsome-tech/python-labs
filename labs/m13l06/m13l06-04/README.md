# m13l06-04 · What replace actually returns

**Lesson:** [More String Methods](https://learnsome.tech/learn/python-course/m13l06) (lesson 13.6, module 13: Flow Of Control) · Pro  
**Check:** Graded

## Goal

You can test what a string starts with, ends with or is made of, and build up conditions from string methods such as startswith, endswith, replace and isdigit.

In the lesson: Start with the string of a minus sign and three digits, and delete the minus sign. The result is the digits on their own. Ask for the same deletion again and nothing changes, which is exactly what you want when you are not sure whether the sign was there. Now take a string with four dots. Delete the first two and the last two survive. Finally spell every dot out in words. There is the surprise: the string begins with a dot, so the answer begins with a space and the word dot. Always check the ends of a string when you are picking it apart.

## Files

- [`starter/shell-what-replace-actually-returns.py`](starter/shell-what-replace-actually-returns.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m13l06/m13l06-04/starter`
2. Read `shell-what-replace-actually-returns.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   s = '-123'
   t = s.replace('-', '', 1)
   t
   t = t.replace('-', '', 1)
   t
   u = '.2.3.4.'
   u.replace('.', '', 2)
   u.replace('.', ' dot ', 5)
   ```
4. Run it: `python3 -i < shell-what-replace-actually-returns.py`.
5. Check it from the repository root: `./check m13l06-04`.

## Expected output

```text
'123'
'123'
'23.4.'
' dot 2 dot 3 dot 4 dot '
```

## How to check

`./check m13l06-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-what-replace-actually-returns.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m13l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
