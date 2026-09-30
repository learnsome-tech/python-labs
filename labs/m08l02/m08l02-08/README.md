# m08l02-08 · floatFormat.py, the first half

**Lesson:** [Exponents, Roots And Float Formats](https://learnsome.tech/learn/python-course/m08l02) (lesson 8.2, module 8: Numbers In Depth) · Pro  
**Check:** Graded

## Goal

You can raise numbers to powers, take square roots with a fractional exponent or with the math module, and round a float for display with the format function or a format string, without changing the value itself.

In the lesson: The tutorial ships all of this as a program called floatFormat dot py. Here is its first half. The third and fourth lines use the format function twice inside a single print call, so one line of output shows the raw value beside two rounded versions. Then two fresh values, printed as they are, for comparison. The next print uses the format method with empty braces, substituting in order. The last substitutes by name from the locals dictionary, and gives an identical line. Run the module and read the five lines carefully. The second half of the file, which is not on screen, prints the same twenty digit experiment we are about to do by hand.

## Files

- [`starter/floatFormat.py`](starter/floatFormat.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l02/m08l02-08/starter`
2. Read `floatFormat.py` the way the lesson builds it:
   - Lines 1–4: the format function twice
   - Lines 5–9: in order
   - Lines 10–11: by name from the locals dictionary
3. Run it: `python3 floatFormat.py`.
4. Check it from the repository root: `./check m08l02-08`.

## Expected output

```text
23.457413902458498 to 5 places: 23.45741 to 2 places: 23.46
x: 2.876543 y: 16.3591
x long: 2.87654, x short: 2.877, y: 16.36.
Same from locals dictionary:
x long: 2.87654, x short: 2.877, y: 16.36.
```

## How to check

`./check m08l02-08` copies `starter/` into a scratch directory and runs `python3 floatFormat.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
