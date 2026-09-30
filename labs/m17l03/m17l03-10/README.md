# m17l03-10 · During handling of the above exception

**Lesson:** [Reading A Traceback Like A Professional](https://learnsome.tech/learn/python-course/m17l03) (lesson 17.3, module 17: Errors, Exceptions And Debugging) · Pro  
**Check:** Graded

## Goal

You can read a multi-frame traceback bottom up, tell your own frames from a library's, recognise the errors that arrive before execution starts, and name the likely cause behind each of the common exception types.

In the lesson: Last shape to recognise. This handler catches a missing key and tries the name in lower case instead, which is fine until that fails too. Now you get two tracebacks stacked up, joined by the sentence during handling of the above exception, another exception occurred. Read them in printed order, because that is the order they happened in: the first is the original failure, and the second is what went wrong while you were dealing with it. The exception that ends the program is the last one. And nobody wrote the word from here, so Python is not claiming one caused the other, only that the second arrived while the first was being handled.

## Files

- [`starter/chained.py`](starter/chained.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m17l03/m17l03-10/starter`
2. Read `chained.py`.
3. Run it: `python3 chained.py`.
4. Check it from the repository root: `./check m17l03-10`.

## Expected output

```text
7
Traceback (most recent call last):
  File "chained.py", line 5, in count_for
    return counts[name]
           ~~~~~~^^^^^^
KeyError: 'Bo'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "chained.py", line 10, in <module>
    print(count_for('Bo'))
          ~~~~~~~~~^^^^^^
  File "chained.py", line 7, in count_for
    return counts[name.lower()]
           ~~~~~~^^^^^^^^^^^^^^
KeyError: 'bo'
```

## How to check

`./check m17l03-10` copies `starter/` into a scratch directory and runs `python3 chained.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m17l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
