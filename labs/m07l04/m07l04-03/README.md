# m07l04-03 · Letting the user choose the count

**Lesson:** [Repeat Loops And Successive Modification](https://learnsome.tech/learn/python-course/m07l04) (lesson 7.4, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can write a simple repeat loop whose loop variable you never use, and build a loop that modifies a variable of your own on every pass, tracing its value pass by pass.

In the lesson: The user can choose the number of repetitions. The example program repeat two reads a line with the input function, converts those digits into a whole number with the int function, and stores the result in n. The range function is then handed n instead of a fixed number. When I ran it I typed three, so the body ran three times. Notice how little actually changed. The loop heading still asks for a range, and the body still ignores the loop variable completely. Only the count now comes from outside the program.

## Files

- [`starter/input.txt`](starter/input.txt): what the program reads on standard input
- [`starter/repeat2.py`](starter/repeat2.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-03/starter`
2. Read `repeat2.py` the way the lesson builds it:
   - Lines 1: repeat two
   - Lines 2–3: the input function
   - Lines 4–5: the body still ignores
3. Run it: `python3 repeat2.py` (with `input.txt` on standard input: `< input.txt`).
4. Check it from the repository root: `./check m07l04-03`.

## Expected output

```text
Enter the number of times to repeat: This is repetitious!
This is repetitious!
This is repetitious!
```

## How to check

`./check m07l04-03` copies `starter/` into a scratch directory and runs `python3 repeat2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
