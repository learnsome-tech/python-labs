# m19l03-04 · Sorting by a rule of your own

**Lesson:** [Sorting, Keys And Lambdas](https://learnsome.tech/learn/python-course/m19l03) (lesson 19.3, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can sort anything by any rule using sorted with a key function, write a lambda for that key, and use stability to sort by two rules in turn.

In the lesson: Try three keys on those words. Passing len sorts by length, shortest first. Passing the method str dot lower makes Python compare lower cased copies, which folds the cases together and gives the order a person expects, while the words themselves keep their capitals. Reverse is a separate argument, and it does the sensible thing with the key. And when no built in function will do, write a lambda: this one returns the last letter of each word, so the words come out ordered by their final letter. That is the pattern for everything. Decide what each item should be judged by, write the one expression that produces it, and hand it over as key.

## Files

- [`starter/shell-sorting-by-a-rule-of-your-own.py`](starter/shell-sorting-by-a-rule-of-your-own.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l03/m19l03-04/starter`
2. Read `shell-sorting-by-a-rule-of-your-own.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   words = ['pear', 'Fig', 'banana', 'kiwi']
   sorted(words, key=len)
   sorted(words, key=str.lower)
   sorted(words, key=len, reverse=True)
   sorted(words, key=lambda w: w[-1])
   ```
4. Run it: `python3 -i < shell-sorting-by-a-rule-of-your-own.py`.
5. Check it from the repository root: `./check m19l03-04`.

## Expected output

```text
['Fig', 'pear', 'kiwi', 'banana']
['banana', 'Fig', 'kiwi', 'pear']
['banana', 'pear', 'kiwi', 'Fig']
['banana', 'Fig', 'kiwi', 'pear']
```

## How to check

`./check m19l03-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-sorting-by-a-rule-of-your-own.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
