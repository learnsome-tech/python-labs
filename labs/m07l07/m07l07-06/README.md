# m07l07-06 · One line from a loop, with a surprise

**Lesson:** [The Print Function Keyword End](https://learnsome.tech/learn/python-course/m07l07) (lesson 7.7, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can use the print function's end keyword parameter, alone or together with sep, to print several things on one line from inside a loop and still finish the line properly.

In the lesson: Here is that loop. The function walks the list and prints each item with end set to a single space, so the three fruit names come out along one line, separated by spaces, which is what we asked for. But there is a print after the call, and look what happens: everything arrives on one line, the sentence included. Work out why before I say it. The last pass of the loop suppressed its newline too, so the line was never finished, and the next print carried straight on from there. The loop does not know it is on its last pass, and it does nothing special there.

## Files

- [`starter/endSpace1.py`](starter/endSpace1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l07/m07l07-06/starter`
2. Read `endSpace1.py` the way the lesson builds it:
   - Lines 1–3: end set to a single space
   - Lines 4–6: a print after the call
3. Run it: `python3 endSpace1.py`.
4. Check it from the repository root: `./check m07l07-06`.

## Expected output

```text
apple banana pear This may not be what you expected!
```

## How to check

`./check m07l07-06` copies `starter/` into a scratch directory and runs `python3 endSpace1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
