# m09l05-03 · Append is not the same as concatenation

**Lesson:** [Appending To Lists, Sets, Constructors](https://learnsome.tech/learn/python-course/m09l05) (lesson 9.5, module 9: Objects And Methods) · Pro  
**Check:** Graded

## Goal

You can grow a list with append inside a loop, explain why that differs from concatenation, build a set to remove duplicates, and recognise a type name used as a constructor.

In the lesson: Compare the two ways of getting a longer list, because they are easy to confuse. The plus sign concatenates: it builds a third list out of the two operands and hands that back, so the original is untouched, exactly like adding strings. If you want to keep the answer you must assign it to a name. Now append instead. Nothing is printed, because the returned value is None, and yet the list has changed in place. Also notice that the plus sign needs a list on both sides, while append takes the single element itself. Concatenation makes something new; append alters what you already have.

## Files

- [`starter/shell-append-is-not-the-same-as-concatenation.py`](starter/shell-append-is-not-the-same-as-concatenation.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m09l05/m09l05-03/starter`
2. Read `shell-append-is-not-the-same-as-concatenation.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   words = ['animal']
   words + ['food']
   words
   words.append('food')
   words
   ```
4. Run it: `python3 -i < shell-append-is-not-the-same-as-concatenation.py`.
5. Check it from the repository root: `./check m09l05-03`.

## Expected output

```text
['animal', 'food']
['animal']
['animal', 'food']
```

## How to check

`./check m09l05-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-append-is-not-the-same-as-concatenation.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m09l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
