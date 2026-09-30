# m19l03-05 · Tuples, dictionaries and the second field

**Lesson:** [Sorting, Keys And Lambdas](https://learnsome.tech/learn/python-course/m19l03) (lesson 19.3, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can sort anything by any rule using sorted with a key function, write a lambda for that key, and use stability to sort by two rules in turn.

In the lesson: Now the case you will actually meet: a list of tuples. With no key at all, tuples compare position by position, first field first, and ties broken by the second, which is often exactly right. To sort by the number instead, the lambda takes one tuple and returns its second field. A dictionary is the same job with one extra step. Sorting a dictionary gives you its keys, in order, which is sometimes all you want. To sort by value, ask for its items, which gives you key and value pairs, and take the second field of each pair. There is your report ordered by age, and swapping the one to a zero orders it by name instead.

## Files

- [`starter/shell-tuples-dictionaries-and-the-second-field.py`](starter/shell-tuples-dictionaries-and-the-second-field.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l03/m19l03-05/starter`
2. Read `shell-tuples-dictionaries-and-the-second-field.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   people = [('Ada', 36), ('Alan', 41), ('Grace', 36)]
   sorted(people)
   sorted(people, key=lambda p: p[1])
   ages = {'ada': 36, 'alan': 41, 'grace': 36}
   sorted(ages)
   sorted(ages.items(), key=lambda pair: pair[1])
   ```
4. Run it: `python3 -i < shell-tuples-dictionaries-and-the-second-field.py`.
5. Check it from the repository root: `./check m19l03-05`.

## Expected output

```text
[('Ada', 36), ('Alan', 41), ('Grace', 36)]
[('Ada', 36), ('Grace', 36), ('Alan', 41)]
['ada', 'alan', 'grace']
[('ada', 36), ('grace', 36), ('alan', 41)]
```

## How to check

`./check m19l03-05` copies `starter/` into a scratch directory and runs `python3 -i < shell-tuples-dictionaries-and-the-second-field.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
