# m05l03-07 · A literal brace: double it

**Lesson:** [The String Format Method](https://learnsome.tech/learn/python-course/m05l03) (lesson 5.3, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can build a string with the format method, substituting values into replacement fields by position, repeating a field, and showing a literal brace.

In the lesson: A technical point. Since braces have special meaning in a format string, there must be a rule if you want braces to appear in the final formatted string. The rule is to double the braces. The example code format braces dot py makes the name set string refer to a sentence describing a set. Look closely at that format string: the initial and final doubled braces generate one literal brace each, while the single pairs between them are ordinary replacement fields taking the values of a and b. Count the braces from the outside in. The printed result has the numbers inside real braces.

## Files

- [`starter/formatBraces.py`](starter/formatBraces.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-07/starter`
2. Read `formatBraces.py`.
3. Notes from the lesson:
   - Line 5: doubled braces make one literal brace; the inner pair is a field
4. Run it: `python3 formatBraces.py`.
5. Check it from the repository root: `./check m05l03-07`.

## Expected output

```text
The set is {5, 9}.
```

## How to check

`./check m05l03-07` copies `starter/` into a scratch directory and runs `python3 formatBraces.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
