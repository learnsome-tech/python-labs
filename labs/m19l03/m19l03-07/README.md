# m19l03-07 · min, max, and the one that has no key

**Lesson:** [Sorting, Keys And Lambdas](https://learnsome.tech/learn/python-course/m19l03) (lesson 19.3, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can sort anything by any rule using sorted with a key function, write a lambda for that key, and use stability to sort by two rules in turn.

In the lesson: The key argument is not only for sorting. Min and max take the same argument and mean the same thing by it: three words, and the shortest and the longest come straight out. Try the same thing on sum and Python refuses, because sum has no key argument, and this catches people who assume the three go together. Sum adds the things you give it, so you give it the numbers you want added, and the neat way to do that is a generator expression, exactly as in the last lesson. One more useful detail: min and max on an empty list raise an error, unless you supply a default, which is worth knowing before it happens to you in a loop over a file.

## Files

- [`starter/shell-min-max-and-the-one-that-has-no-key.py`](starter/shell-min-max-and-the-one-that-has-no-key.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l03/m19l03-07/starter`
2. Read `shell-min-max-and-the-one-that-has-no-key.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   words = ['pear', 'fig', 'banana']
   min(words, key=len)
   max(words, key=len)
   sum(words, key=len)
   sum(len(w) for w in words)
   min([], default='nothing')
   ```
4. Run it: `python3 -i < shell-min-max-and-the-one-that-has-no-key.py`.
5. Check it from the repository root: `./check m19l03-07`.

## Expected output

```text
'fig'
'banana'
Traceback (most recent call last):
TypeError: sum() got an unexpected keyword argument 'key'
13
'nothing'
```

## How to check

`./check m19l03-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-min-max-and-the-one-that-has-no-key.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
