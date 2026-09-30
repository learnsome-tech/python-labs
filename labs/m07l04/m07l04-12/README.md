# m07l04-12 · The same loop, wrapped in a function

**Lesson:** [Repeat Loops And Successive Modification](https://learnsome.tech/learn/python-course/m07l04) (lesson 7.4, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can write a simple repeat loop whose loop variable you never use, and build a loop that modifies a variable of your own on every pass, tracing its value pass by pass.

In the lesson: Finally, wrap the loop in a function, so the idea can be reused and tested with different data. Number entries four defines number list, which takes a parameter items and does just what the loose code did. Main calls it twice. Execution starts at the very last line, because everything above it is only a definition. Main begins, and the first call sets the formal parameter items to the four colour names, after which the function behaves exactly like number entries three, except that control now returns to main. Main prints an empty line, then calls number list again with three fruit names, so the loop runs one time fewer. Then main has nothing left to do.

## Files

- [`starter/numberEntries4.py`](starter/numberEntries4.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-12/starter`
2. Read `numberEntries4.py` the way the lesson builds it:
   - Lines 1–8: which takes a parameter items
   - Lines 9–15: Main calls it twice
3. Notes from the lesson:
   - Line 11: this call sets the formal parameter items to the four colours
   - Line 13: this call sets items to the shorter list of three fruit names
4. Run it: `python3 numberEntries4.py`.
5. Check it from the repository root: `./check m07l04-12`.

## Expected output

```text
1 red
2 orange
3 yellow
4 green

1 apples
2 pears
3 bananas
```

## How to check

`./check m07l04-12` copies `starter/` into a scratch directory and runs `python3 numberEntries4.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
