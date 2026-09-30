# m05l03-04 · Dropping the extra name

**Lesson:** [The String Format Method](https://learnsome.tech/learn/python-course/m05l03) (lesson 5.3, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can build a string with the format method, substituting values into replacement fields by position, repeating a field, and showing a literal brace.

In the lesson: The identifier greeting was introduced to break the operations into a clearer sequence of steps, which was a good idea while the syntax was new. But since its value is referenced only once, it can be eliminated, giving this more concise version. The format method produces a string, and a string is exactly what the print function wants, so the whole expression goes straight inside the print call. Both forms are correct. When a name helps a reader follow the steps, keep it; when it is used once, right where it was made, it is usually clutter.

## Files

- [`starter/hello_you3b.py`](starter/hello_you3b.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-04/starter`
2. Read `hello_you3b.py`.
3. Run it: `python3 hello_you3b.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m05l03-04`.

## Expected output

```text
Enter your name: Hello Anna!
```

## How to check

`./check m05l03-04` copies `starter/` into a scratch directory and runs `python3 hello_you3b.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
