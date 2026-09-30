# m07l06-02 · A very natural mistake

**Lesson:** [Playing Computer](https://learnsome.tech/learn/python-course/m07l06) (lesson 7.6, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can trace a loop or a nest of function calls by hand, keeping one table row per executed line, and use that table to locate the exact line where a logical error appears.

In the lesson: Here is a common error in writing the number list function. All the right ingredients are in the function body, and the call at the bottom passes a list of three fruit names, but one line has slipped from before the loop to inside it. Run it and every line is numbered one. Now, you can see from the output that something is wrong, but the output alone does not tell you which line is at fault. There is even an increment sitting there that looks perfectly correct. Do not guess. Play computer on this call and the culprit gives itself up.

## Files

- [`starter/numberEntriesWRONG.py`](starter/numberEntriesWRONG.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l06/m07l06-02/starter`
2. Read `numberEntriesWRONG.py` the way the lesson builds it:
   - Lines 1–6: the function body
   - Lines 7–8: the call at the bottom
3. Notes from the lesson:
   - Line 4: this initialisation has slipped inside the loop body
4. Run it: `python3 numberEntriesWRONG.py`.
5. Check it from the repository root: `./check m07l06-02`.

## Expected output

```text
1 apples
1 pears
1 bananas
```

## How to check

`./check m07l06-02` copies `starter/` into a scratch directory and runs `python3 numberEntriesWRONG.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
