# m20l04-02 · You have been calling dunder methods all along

**Lesson:** [Dunder Methods, And Making Objects Pythonic](https://learnsome.tech/learn/python-course/m20l04) (lesson 20.4, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can give a class a useful repr and str, define equality and hashing consistently, make an object work with len, indexing and a for loop, and reach for a dataclass when the class is plain data.

In the lesson: Watch the trick from the outside first. Ask for the length of a string and you get five. Now call the dunder yourself and you get the same five, because that is all the length function ever did: it looked up dunder len on the object and called it. Addition is the same story, both for numbers and for the same plus sign on lists. The list version concatenates, because list's dunder add concatenates, while the integer version adds, and the plus sign itself has no opinion at all. Even the class an object came from is a dunder attribute. Nobody writes the long forms in real code; they are just proof that the short forms are calls to methods you are allowed to write yourself.

## Files

- [`starter/shell-you-have-been-calling-dunder-methods-all-alo.py`](starter/shell-you-have-been-calling-dunder-methods-all-alo.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l04/m20l04-02/starter`
2. Read `shell-you-have-been-calling-dunder-methods-all-alo.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   len('hello')
   'hello'.__len__()
   2 + 3
   (2).__add__(3)
   [1, 2] + [3]
   [1, 2].__add__([3])
   'ab'.__class__
   ```
4. Run it: `python3 -i < shell-you-have-been-calling-dunder-methods-all-alo.py`.
5. Check it from the repository root: `./check m20l04-02`.

## Expected output

```text
5
5
5
5
[1, 2, 3]
[1, 2, 3]
<class 'str'>
```

## How to check

`./check m20l04-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-you-have-been-calling-dunder-methods-all-alo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
