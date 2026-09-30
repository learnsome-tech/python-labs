# m05l03-09 · Reusing and reordering parameters

**Lesson:** [The String Format Method](https://learnsome.tech/learn/python-course/m05l03) (lesson 5.3, module 5: Programs, Input, Output) · Pro  
**Check:** Graded

## Goal

You can build a string with the format method, substituting values into replacement fields by position, repeating a field, and showing a literal brace.

In the lesson: Predict the results of the example file arith dot py if you enter five and six, then check yourself by running it. Here the numbers referring to the parameter positions are necessary, because the parameters are both repeated and used out of order. Every place the string has the field numbered zero, format substitutes the initial parameter; wherever the field numbered one appears, the second parameter goes in. Parameter zero and parameter one each appear twice, once in the sum and once in the product. Notice too that the format string is held in its own variable, and format is called on that variable later. Try the program with other data.

## Files

- [`starter/arith.py`](starter/arith.py): the listing from the lesson
- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-09/starter`
2. Read `arith.py` the way the lesson builds it:
   - Lines 1–6: Predict the results
   - Lines 7–9: held in its own variable
3. Notes from the lesson:
   - Line 7: parameter zero and parameter one each appear twice
4. Run it: `python3 arith.py` (with `input.txt` on standard input: `< input.txt`).
5. Check it from the repository root: `./check m05l03-09`.

## Expected output

```text
Enter an integer: Enter another integer: 5 + 6 = 11; 5 * 6 = 30.
```

## How to check

`./check m05l03-09` copies `starter/` into a scratch directory and runs `python3 arith.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
