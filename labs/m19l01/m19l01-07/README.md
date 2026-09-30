# m19l01-07 · Nesting them inside each other

**Lesson:** [Lists, Tuples, Sets, Dicts: Choosing One](https://learnsome.tech/learn/python-course/m19l01) (lesson 19.1, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can choose between a list, a tuple, a set and a dictionary for a given job, say what each costs to search, and explain why a tuple can be a dictionary key when a list cannot.

In the lesson: These four nest freely, and real programs are made of the combinations. Here is a list of dictionaries, each holding a name and a set of languages, which is the commonest shape you will meet, and the shape that comes back from reading most data files. Run it and read the four lines. Looping over the list gives you one dictionary at a time. Then the same data is rebuilt as a dictionary keyed by name, so a lookup by name is immediate rather than a search through the list. Notice the last line: comparing two sets ignores the order entirely, so the test passes even though the languages were written the other way round. That is a set doing what a list could not.

## Files

- [`starter/people.py`](starter/people.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l01/m19l01-07/starter`
2. Read `people.py`.
3. Notes from the lesson:
   - Line 3: a list of dictionaries: the commonest shape in real code
   - Line 11: rebuilt as a dictionary keyed by name, for fast lookup
4. Run it: `python3 people.py`.
5. Check it from the repository root: `./check m19l01-07`.

## Expected output

```text
Ada knows 2 languages
Alan knows 3 languages
['Ada', 'Alan']
True
```

## How to check

`./check m19l01-07` copies `starter/` into a scratch directory and runs `python3 people.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
