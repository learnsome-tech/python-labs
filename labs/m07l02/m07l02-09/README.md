# m07l02-09 · hello_you4.py, with a dictionary reference

**Lesson:** [Dictionaries And String Formatting](https://learnsome.tech/learn/python-course/m07l02) (lesson 7.2, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can build strings with the format method and a dictionary unpacked by two stars, and use locals or an f-string to drop local variable values straight into a format string.

In the lesson: The example program hello you four does the same thing as the earlier hello you versions, but with a dictionary reference. The name the user types is stored in the variable person. The format string mentions person inside braces, and the format method is handed locals, unpacked with two stars, so the value is pulled straight out of the local namespace by name. Here the user types Anna, and the greeting comes back with the name in place. Compare this with the earlier versions that glued the name on with plus signs, and decide for yourself which one you would rather read six months from now.

## Files

- [`starter/hello_you4.py`](starter/hello_you4.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l02/m07l02-09/starter`
2. Read `hello_you4.py`.
3. Run it: `python3 hello_you4.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m07l02-09`.

## Expected output

```text
Enter your name: Hello, Anna!
```

## How to check

`./check m07l02-09` copies `starter/` into a scratch directory and runs `python3 hello_you4.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
