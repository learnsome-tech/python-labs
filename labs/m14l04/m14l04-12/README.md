# m14l04-12 · Where the strange syntax pays for itself

**Lesson:** [Any Type As A Condition](https://learnsome.tech/learn/python-course/m14l04) (lesson 14.4, module 14: While Loops) · Pro  
**Check:** Graded

## Goal

You can say which values of any type Python treats as False, use the Pythonic test for an empty collection, and recognise the bugs that arise when a comparison and an or are combined carelessly.

In the lesson: This strange syntax was included in Python to allow code like this example program. The default colour is red. The user is asked for a colour and may say nothing at all. The next line takes the user's colour or the default. If the user typed something, that string is nonempty and therefore True, so the colour is whatever they typed. If they pressed Enter, the answer is the empty string, which is False, so the colour falls back to the default. Here is the program run with pressing Enter at once. Again, this may be useful to experienced programmers, but the syntax can certainly cause difficult bugs, particularly for beginners.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/orNotBoolean.py`](starter/orNotBoolean.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m14l04/m14l04-12/starter`
2. Read `orNotBoolean.py`.
3. Run it: `python3 orNotBoolean.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m14l04-12`.

## Expected output

```text
Enter a color, or just press Enter for the default: The color is red
```

## How to check

`./check m14l04-12` copies `starter/` into a scratch directory and runs `python3 orNotBoolean.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m14l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
