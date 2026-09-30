# m07l02-02 · Words in braces, and keyword parameters

**Lesson:** [Dictionaries And String Formatting](https://learnsome.tech/learn/python-course/m07l02) (lesson 7.2, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can build strings with the format method and a dictionary unpacked by two stars, and use locals or an f-string to drop local variable values straight into a format string.

In the lesson: The first string could be constructed and printed as follows. There are several new ideas here. Note the form of the string assigned the name numberFormat: it has the English words for numbers in braces, where we want the Spanish definitions substituted. That is unlike the format strings you met earlier, which had empty braces or a number inside. The second line uses method calling syntax: an object, a period, the method name, and further parameters in parentheses. Here the object is the string numberFormat and the method is named format. The parameters are all keyword parameters, like the separator keyword you have already used with print, and the keywords are chosen to be exactly the words that appear in braces. Then we print the result, and the substitutions land where the braces were.

## Files

- [`starter/numberFormat.py`](starter/numberFormat.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l02/m07l02-02/starter`
2. Read `numberFormat.py` the way the lesson builds it:
   - Lines 1: the string assigned the name numberFormat
   - Lines 2: The second line uses method calling syntax
   - Lines 3: print the result
3. Run it: `python3 numberFormat.py`.
4. Check it from the repository root: `./check m07l02-02`.

## Expected output

```text
Count in Spanish: uno, dos, tres, ...
```

## How to check

`./check m07l02-02` copies `starter/` into a scratch directory and runs `python3 numberFormat.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
