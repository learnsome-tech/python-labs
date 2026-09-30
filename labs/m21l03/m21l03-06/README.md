# m21l03-06 · Random numbers, and the same ones again

**Lesson:** [Dates, Times And Random](https://learnsome.tech/learn/python-course/m21l03) (lesson 21.3, module 21: Files, Formats And The Standard Library) · Pro  
**Check:** Graded

## Goal

You can make and compare dates, do arithmetic with timedelta, format and parse them with strftime and strptime, and generate random numbers you can reproduce with a seed.

In the lesson: The random module is the other half of this lesson. The random function gives a float between zero and one. Randint gives a whole number between two bounds with both ends included, which is unlike range and catches people out. Choice picks one item from any sequence. But look at the top of the program and at the fourth line of output. The seed function fixes the starting point of the generator, so this program prints the same three answers every single time it runs, and asking for a seed again rewinds it. That is how you test a program that uses randomness: seed it, and a failure you can reproduce is a failure you can fix.

## Files

- [`starter/randomBasics.py`](starter/randomBasics.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m21l03/m21l03-06/starter`
2. Read `randomBasics.py`.
3. Notes from the lesson:
   - Line 3: seed fixes the starting point, so every run matches
   - Line 5: randint includes both ends, unlike range
4. Run it: `python3 randomBasics.py`.
5. Check it from the repository root: `./check m21l03-06`.

## Expected output

```text
0.32383276483316237
2
paper
0.32383276483316237
```

## How to check

`./check m21l03-06` copies `starter/` into a scratch directory and runs `python3 randomBasics.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m21l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
