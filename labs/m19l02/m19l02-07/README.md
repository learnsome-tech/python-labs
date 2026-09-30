# m19l02-07 · Generator expressions: the lazy form

**Lesson:** [Comprehensions](https://learnsome.tech/learn/python-course/m19l02) (lesson 19.2, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can turn a build-a-list loop into a list comprehension with an optional filter, write dictionary and set comprehensions, and say when a plain loop is the clearer choice.

In the lesson: One more form, and it is the useful one for large data. Round brackets instead of square give you a generator expression, and the result is not a list at all. Nothing has been calculated yet. Each value is worked out when it is asked for the next one, and never stored. That is why you can write a generator expression over a million items without using any memory. When a generator expression is the only argument to a function you can leave its brackets out entirely, which is why summing squares reads so cleanly. But notice the last two lines. Asking for a list gives you the three that were left, and asking a second time gives nothing at all. A generator can be walked once, and the next lesson is all about that.

## Files

- [`starter/shell-generator-expressions-the-lazy-form.py`](starter/shell-generator-expressions-the-lazy-form.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l02/m19l02-07/starter`
2. Read `shell-generator-expressions-the-lazy-form.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   g = (x*x for x in range(1, 6))
   type(g).__name__
   next(g)
   next(g)
   sum(x*x for x in range(1, 6))
   list(g)
   list(g)
   ```
4. Run it: `python3 -i < shell-generator-expressions-the-lazy-form.py`.
5. Check it from the repository root: `./check m19l02-07`.

## Expected output

```text
'generator'
1
4
55
[9, 16, 25]
[]
```

## How to check

`./check m19l02-07` copies `starter/` into a scratch directory and runs `python3 -i < shell-generator-expressions-the-lazy-form.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
