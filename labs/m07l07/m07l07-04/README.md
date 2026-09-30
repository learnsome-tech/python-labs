# m07l07-04 · Both versions side by side

**Lesson:** [The Print Function Keyword End](https://learnsome.tech/learn/python-course/m07l07) (lesson 7.7, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can use the print function's end keyword parameter, alone or together with sep, to print several things on one line from inside a loop and still finish the line properly.

In the lesson: The example file end space zero puts both versions in the same program, so you can see the claim tested rather than asserted. The first function holds the plain version, the second function holds the end keyword version, and main labels each one before calling it. Run it and the two blocks of output are word for word the same. Notice that the words on one line came from three different calls to print, and nothing in the output betrays that. Once a newline has been suppressed, output carries on from where the last call stopped.

## Files

- [`starter/endSpace0.py`](starter/endSpace0.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l07/m07l07-04/starter`
2. Read `endSpace0.py` the way the lesson builds it:
   - Lines 1–5: the plain version
   - Lines 6–13: the end keyword version
   - Lines 14–21: main labels each one
3. Run it: `python3 endSpace0.py`.
4. Check it from the repository root: `./check m07l07-04`.

## Expected output

```text
print1 results:
all on same line
different line
print2 has the same results:
all on same line
different line
```

## How to check

`./check m07l07-04` copies `starter/` into a scratch directory and runs `python3 endSpace0.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
