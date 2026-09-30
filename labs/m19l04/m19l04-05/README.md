# m19l04-05 · Why it uses no memory

**Lesson:** [Iterators And Generators](https://learnsome.tech/learn/python-course/m19l04) (lesson 19.4, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can explain what a for loop does in terms of iter and next, write a generator function with yield, and say why a generator costs no memory however long its sequence is.

In the lesson: Here is the reason this matters. A million squares in a list, and a generator over the same million squares, and we measure both of them. The list is eight megabytes, because it is a million numbers held at once, and that is before counting the numbers themselves. The generator is under a kilobyte: it is one paused frame, holding where it got to, and its size would be identical for a million or a billion. The third line proves it is not a trick: both add up to exactly the same total. The rule to take away is that a generator trades memory for a promise, and the promise is that you will take the values one at a time and not ask for them twice.

## Files

- [`starter/memory.py`](starter/memory.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l04/m19l04-05/starter`
2. Read `memory.py`.
3. Notes from the lesson:
   - Line 8: a million integers, all held at once
   - Line 9: one paused frame, whatever the length of the sequence
4. Run it: `python3 memory.py`.
5. Check it from the repository root: `./check m19l04-05`.

## Expected output

```text
list megabytes: 8
generator under a kilobyte: True
both add up to the same total: True
```

## How to check

`./check m19l04-05` copies `starter/` into a scratch directory and runs `python3 memory.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
