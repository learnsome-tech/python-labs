# m19l04-06 · Things that were lazy all along

**Lesson:** [Iterators And Generators](https://learnsome.tech/learn/python-course/m19l04) (lesson 19.4, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can explain what a for loop does in terms of iter and next, write a generator function with yield, and say why a generator costs no memory however long its sequence is.

In the lesson: Once you know about laziness you start seeing it everywhere, because three tools you already use are built on it. Type a million long range into the Shell and it does not print a million numbers; it prints itself, because a range is not a list and never was. It works out each number as you ask. Asking for a list is how you force it, and that is the only time the numbers exist. Zip pairs two sources and is lazy in the same way, giving you pairs of one from each as you walk it. Enumerate counts as it goes, handing you a position and a value together, and you can tell it to start at one instead of zero. All three are objects that produce, not collections that hold.

## Files

- [`starter/shell-things-that-were-lazy-all-along.py`](starter/shell-things-that-were-lazy-all-along.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l04/m19l04-06/starter`
2. Read `shell-things-that-were-lazy-all-along.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   range(1000000)
   type(range(5)).__name__
   list(range(3))
   z = zip([1, 2, 3], 'abc')
   type(z).__name__
   list(z)
   list(enumerate(['a', 'b']))
   list(enumerate(['a', 'b'], start=1))
   ```
4. Run it: `python3 -i < shell-things-that-were-lazy-all-along.py`.
5. Check it from the repository root: `./check m19l04-06`.

## Expected output

```text
range(0, 1000000)
'range'
[0, 1, 2]
'zip'
[(1, 'a'), (2, 'b'), (3, 'c')]
[(0, 'a'), (1, 'b')]
[(1, 'a'), (2, 'b')]
```

## How to check

`./check m19l04-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-things-that-were-lazy-all-along.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
