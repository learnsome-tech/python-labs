# m09l01-04 · Lower case, and the other case methods

**Lesson:** [Objects, Methods And String Case](https://learnsome.tech/learn/python-course/m09l01) (lesson 9.1, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can call a method on a string with the object dot method syntax, explain why a string method returns a new string instead of changing the original, and use upper, lower, capitalize, title and count.

In the lesson: Another string method is lower, analogous to upper but producing a lowercase result. Test yourself first: how would you write the expression that produces a lowercase version of the string s? Then a harder one. Using s and both lower and upper, how would you build a string that is the lowercase copy followed straight away by the uppercase copy? Both calls return strings, so a plus sign concatenates them. Two more case methods, which the tutorial names in its further reading, fit here too: capitalize, which raises the first letter of the whole string and lowers the rest, and title, which raises the first letter of every word. Notice those two are called on string literals rather than on a variable, because the object before the dot can be anything. And after all that, s itself is untouched.

## Files

- [`starter/shell-lower-case-and-the-other-case-methods.py`](starter/shell-lower-case-and-the-other-case-methods.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l01/m09l01-04/starter`
2. Read `shell-lower-case-and-the-other-case-methods.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   s = 'Hello!'
   s.lower()
   s.lower() + s.upper()
   'hello there'.capitalize()
   'hello there'.title()
   s
   ```
4. Run it: `python3 -i < shell-lower-case-and-the-other-case-methods.py`.
5. Check it from the repository root: `./check m09l01-04`.

## Expected output

```text
'hello!'
'hello!HELLO!'
'Hello there'
'Hello There'
'Hello!'
```

## How to check

`./check m09l01-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-lower-case-and-the-other-case-methods.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
