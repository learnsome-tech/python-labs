# m19l04-02 · Driving the protocol by hand

**Lesson:** [Iterators And Generators](https://learnsome.tech/learn/python-course/m19l04) (lesson 19.4, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can explain what a for loop does in terms of iter and next, write a generator function with yield, and say why a generator costs no memory however long its sequence is.

In the lesson: Do it by hand in the Shell so it stops being abstract. Take an ordinary list and ask it for an iterator. Now call next repeatedly and you get one value at a time, in order. The fourth call has nothing to give, so it raises StopIteration, and that exception is not an error in your program; it is the agreed way of saying the sequence has finished. Look at the type of the iterator: it is a separate object called a list iterator, not the list. The list is the collection, and the iterator is the position in it. And asking the list for an iterator twice gives you a fresh one every time, which is why you can loop over the same list again and again.

## Files

- [`starter/shell-driving-the-protocol-by-hand.py`](starter/shell-driving-the-protocol-by-hand.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l04/m19l04-02/starter`
2. Read `shell-driving-the-protocol-by-hand.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   nums = [10, 20, 30]
   it = iter(nums)
   next(it)
   next(it)
   next(it)
   next(it)
   type(it).__name__
   iter(nums) is iter(nums)
   ```
4. Run it: `python3 -i < shell-driving-the-protocol-by-hand.py`.
5. Check it from the repository root: `./check m19l04-02`.

## Expected output

```text
10
20
30
Traceback (most recent call last):
StopIteration
'list_iterator'
False
```

## How to check

`./check m19l04-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-driving-the-protocol-by-hand.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
