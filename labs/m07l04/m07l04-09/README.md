# m07l04-09 · The crucial line, and the whole loop

**Lesson:** [Repeat Loops And Successive Modification](https://learnsome.tech/learn/python-course/m07l04) (lesson 7.4, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can write a simple repeat loop whose loop variable you never use, and build a loop that modifies a variable of your own on every pass, tracing its value pass by pass.

In the lesson: One changed line gives us number entries three, and now it is correct. The last line of the body says number is assigned number plus one. The right hand side is worked out first, using the current value, and the answer is stored back into the same variable. So on the first pass one becomes two, and on the second pass two becomes three. Run it and the four lines are numbered one, two, three, four. The tutorial numbers the lines of this program, because the flow of control jumps about at the end of the loop, and we are going to follow that flow next.

## Files

- [`starter/numberEntries3.py`](starter/numberEntries3.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-09/starter`
2. Read `numberEntries3.py`.
3. Notes from the lesson:
   - Line 5: old value on the right, new value stored back in the same name
4. Run it: `python3 numberEntries3.py`.
5. Check it from the repository root: `./check m07l04-09`.

## Expected output

```text
1 red
2 orange
3 yellow
4 green
```

## How to check

`./check m07l04-09` copies `starter/` into a scratch directory and runs `python3 numberEntries3.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
