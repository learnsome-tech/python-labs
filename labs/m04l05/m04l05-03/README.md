# m04l05-03 · Three names Python refuses

**Lesson:** [Literals, Identifiers And Keywords](https://learnsome.tech/learn/python-course/m04l05) (lesson 4.5, module 4: Data And Expressions) · Pro  
**Check:** Graded

## Goal

You can tell a literal from an identifier, say which character sequences Python allows as a name, avoid the reserved words, and name multi word variables in a conventional way.

In the lesson: Here are three names Python will not take. The first is a reserved word, class, which has a special meaning we come to much later. Python cannot tell whether you are starting a class definition or naming a value, so it stops. The second starts with a digit, and the message names the trouble precisely: the interpreter began reading a number and then found letters glued on to it. The third has blanks in the middle. Python reads the first word as a complete name and then cannot make sense of what follows it. All three are syntax errors, found before a single instruction was carried out. None of them is a comment on your taste in names. They are about what the translator can parse.

## Files

- [`starter/shell-three-names-python-refuses.py`](starter/shell-three-names-python-refuses.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-03/starter`
2. Read `shell-three-names-python-refuses.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   class = 5
   2nd_place = 'silver'
   price at opening = 3
   ```
4. Run it: `python3 -i < shell-three-names-python-refuses.py`.
5. Check it from the repository root: `./check m04l05-03`.

## Expected output

```text
SyntaxError: invalid syntax
SyntaxError: invalid decimal literal
SyntaxError: invalid syntax
```

## How to check

`./check m04l05-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-three-names-python-refuses.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
