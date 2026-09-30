# m19l04-03 · What a for loop really does

**Lesson:** [Iterators And Generators](https://learnsome.tech/learn/python-course/m19l04) (lesson 19.4, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can explain what a for loop does in terms of iter and next, write a generator function with yield, and say why a generator costs no memory however long its sequence is.

In the lesson: Here is the whole of the for statement, written out longhand. At the top, the loop you would write. Underneath, the same loop with the protocol written out by hand: get an iterator, call next inside a try, and break out when StopIteration arrives. Run it and you get the same six lines, three from each. So a for loop calls iter once, calls next until it is refused, catches StopIteration for you, and hands each value to your variable. That is all. Nobody writes the bottom version, but knowing it is there explains everything else in this lesson, including why some things can only be looped over once.

## Files

- [`starter/byhand.py`](starter/byhand.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l04/m19l04-03/starter`
2. Read `byhand.py` the way the lesson builds it:
   - Lines 1–6: the loop you would write
   - Lines 7–14: the same loop with the protocol written out
3. Notes from the lesson:
   - Line 8: the for loop calls iter for you, once
   - Line 12: and catches StopIteration for you, invisibly
4. Run it: `python3 byhand.py`.
5. Check it from the repository root: `./check m19l04-03`.

## Expected output

```text
10
20
30
10
20
30
```

## How to check

`./check m19l04-03` copies `starter/` into a scratch directory and runs `python3 byhand.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
