# m21l04-03 · collections: Counter, defaultdict and namedtuple

**Lesson:** [A Standard Library Tour](https://learnsome.tech/learn/python-course/m21l04) (lesson 21.4, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can name the standard library modules a beginner actually meets, say what each one is for, recognise when a problem belongs to one of them, and look the details up for yourself.

In the lesson: The collections module holds specialised containers. Three of them here. Counter takes any sequence and counts it, which replaces the dictionary and the if statement you would otherwise write, and its most common method answers the top n question directly. The default dict is a dictionary that creates a missing value instead of raising a key error: tell it the values are lists, and appending to a key that does not exist yet works first time. A named tuple is a tuple whose positions have names, so you can write point dot x as well as point at position zero, and it prints itself readably. Any of the three can turn a fiddly ten lines into one.

## Files

- [`starter/collect.py`](starter/collect.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l04/m21l04-03/starter`
2. Read `collect.py` the way the lesson builds it:
   - Lines 1–5: Counter takes any sequence
   - Lines 6–10: the default dict
   - Lines 11–14: A named tuple
3. Run it: `python3 collect.py`.
4. Check it from the repository root: `./check m21l04-03`.

## Expected output

```text
3 [('the', 3), ('cat', 1)]
{3: ['the', 'cat', 'sat', 'the', 'mat', 'the', 'end'], 2: ['on']}
Point(x=3, y=4) 3 4
```

## How to check

`./check m21l04-03` copies `starter/` into a scratch directory and runs `python3 collect.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
