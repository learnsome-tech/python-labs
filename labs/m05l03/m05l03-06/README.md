# m05l03-06 · Format converts types for you

**Lesson:** [The String Format Method](https://learnsome.tech/learn/python-course/m05l03) (lesson 5.3, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can build a string with the format method, substituting values into replacement fields by position, repeating a field, and showing a literal brace.

In the lesson: Sometimes you want a single string, and not just for printing. You can combine pieces with the plus operator, but then all the pieces must be strings, or explicitly converted to strings. An advantage of the format method is that it converts types to string automatically, as the print function does. Here is our addition sentence again, in the example file addition four a dot py. The three values going into the braces are integers, and format turns each of them into text without being asked. Here that saves real work, and the sentence comes out as one value you can store, return, or print.

## Files

- [`starter/addition4a.py`](starter/addition4a.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-06/starter`
2. Read `addition4a.py`.
3. Notes from the lesson:
   - Line 6: x, y and sum are integers; format converts them to text
4. Run it: `python3 addition4a.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m05l03-06`.

## Expected output

```text
Enter an integer: Enter another integer: The sum of 2 and 3 is 5.
```

## How to check

`./check m05l03-06` copies `starter/` into a scratch directory and runs `python3 addition4a.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
