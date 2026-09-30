# m19l04-07 · An iterator is good for one pass

**Lesson:** [Iterators And Generators](https://learnsome.tech/learn/python-course/m19l04) (lesson 19.4, module 19: Data Structures In Depth) · Pro  
**Check:** Graded

## Goal

You can explain what a for loop does in terms of iter and next, write a generator function with yield, and say why a generator costs no memory however long its sequence is.

In the lesson: One last thing, and it is the mistake everybody makes once. Make a generator and collect it into a list, and you get the three values. Ask a second time and you get an empty list. Run it and watch the second line. The generator is finished; it is standing at the end of its sequence and there is nothing behind it. This is not a bug and there is no rewind. The same is true of zip, of enumerate, and of a file you have read to the end. If you need the values twice, either keep them in a list, which costs the memory, or call the generator function again, because a new call makes a new generator. Ranges are the exception, and that is why a range is not an iterator.

## Files

- [`starter/exhaust.py`](starter/exhaust.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m19l04/m19l04-07/starter`
2. Read `exhaust.py`.
3. Notes from the lesson:
   - Line 10: the same generator, already finished: an empty list
   - Line 12: a new call makes a new generator, so this works
4. Run it: `python3 exhaust.py`.
5. Check it from the repository root: `./check m19l04-07`.

## Expected output

```text
[3, 2, 1]
[]
3
2
1
```

## How to check

`./check m19l04-07` copies `starter/` into a scratch directory and runs `python3 exhaust.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m19l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
