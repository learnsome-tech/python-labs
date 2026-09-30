# m21l04-04 · itertools: looping tools you did not write

**Lesson:** [A Standard Library Tour](https://learnsome.tech/learn/python-course/m21l04) (lesson 21.4, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can name the standard library modules a beginner actually meets, say what each one is for, recognise when a problem belongs to one of them, and look the details up for yourself.

In the lesson: The itertools module builds iterators, which you met in the generators lesson. Count is an endless counter from a starting number in steps, and because it never stops you take a slice of it with islice rather than looping over it directly. Cycle repeats a sequence forever, which is how you deal a deck round a table or stripe alternate rows of a table. Combinations gives every unordered pairing of a collection, and its neighbours permutations and product cover the ordered and the every to every cases. These are the loops that are annoying to write correctly and easy to get subtly wrong, already written and already tested. Run it and read the output next to the code.

## Files

- [`starter/itersDemo.py`](starter/itersDemo.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l04/m21l04-04/starter`
2. Read `itersDemo.py`.
3. Run it: `python3 itersDemo.py`.
4. Check it from the repository root: `./check m21l04-04`.

## Expected output

```text
10 15 20 25
['red', 'green', 'red', 'green', 'red']
('a', 'b')
('a', 'c')
('b', 'c')
```

## How to check

`./check m21l04-04` copies `starter/` into a scratch directory and runs `python3 itersDemo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
