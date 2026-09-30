# m19l02-04 · Dictionary and set comprehensions

**Lesson:** [Comprehensions](https://learnsome.tech/learn/python-course/m19l02) (lesson 19.2, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can turn a build-a-list loop into a list comprehension with an optional filter, write dictionary and set comprehensions, and say when a plain loop is the clearer choice.

In the lesson: The same syntax builds the other two containers, and only the punctuation changes. Braces with a key and a value with a colon between them give you a dictionary: every word mapped to its length, in one line. Braces with no colon give you a set, so this one collects the distinct lengths, and the four words produce three numbers because two of them are the same length. My favourite use is turning a dictionary inside out: loop over its items and build a new dictionary swapping each pair, so the values become the keys. And the distinct first letters of the words come out of a set comprehension, sorted so they print in a fixed order, because a set has none.

## Files

- [`starter/shell-dictionary-and-set-comprehensions.py`](starter/shell-dictionary-and-set-comprehensions.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l02/m19l02-04/starter`
2. Read `shell-dictionary-and-set-comprehensions.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   words = ['pear', 'fig', 'banana', 'kiwi']
   {w: len(w) for w in words}
   {len(w) for w in words}
   ages = {'ada': 36, 'alan': 41}
   {value: key for key, value in ages.items()}
   sorted({w[0] for w in words})
   ```
4. Run it: `python3 -i < shell-dictionary-and-set-comprehensions.py`.
5. Check it from the repository root: `./check m19l02-04`.

## Expected output

```text
{'pear': 4, 'fig': 3, 'banana': 6, 'kiwi': 4}
{3, 4, 6}
{36: 'ada', 41: 'alan'}
['b', 'f', 'k', 'p']
```

## How to check

`./check m19l02-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-dictionary-and-set-comprehensions.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
