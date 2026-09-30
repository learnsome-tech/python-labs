# m09l01-02 · A string knows how to shout

**Lesson:** [Objects, Methods And String Case](https://learnsome.tech/learn/python-course/m09l01) (lesson 9.1, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can call a method on a string with the object dot method syntax, explain why a string method returns a new string instead of changing the original, and use upper, lower, capitalize, title and count.

In the lesson: Strings are objects, and strings know how to produce an uppercase version of themselves. Type the assignment, then the call, with a dot between the string and the method name. Here upper is a method associated with strings, a function bound to the string in front of the dot, both logically and now visibly in the notation. The expression calls upper on the string s and returns a new uppercase string based on s. Now the part that catches people out. Strings are immutable, so no string method can change the original string; it can only hand back a new one. Ask for s again and it is exactly what we typed. Store the result of the upper call under a second name, look at that second name, then look at s one more time. The shouting lives in the new name. The original has not moved.

## Files

- [`starter/shell-a-string-knows-how-to-shout.py`](starter/shell-a-string-knows-how-to-shout.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l01/m09l01-02/starter`
2. Read `shell-a-string-knows-how-to-shout.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   s = 'Hello!'
   s.upper()
   s
   s2 = s.upper()
   s2
   s
   ```
4. Run it: `python3 -i < shell-a-string-knows-how-to-shout.py`.
5. Check it from the repository root: `./check m09l01-02`.

## Expected output

```text
'HELLO!'
'Hello!'
'HELLO!'
'Hello!'
```

## How to check

`./check m09l01-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-a-string-knows-how-to-shout.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
