# m07l01-02 · The program spanish1.py

**Lesson:** [Dictionaries](https://learnsome.tech/learn/python-course/m07l01) (lesson 7.1, module 7: Dictionaries And Loops) · Pro  
**Check:** Graded

## Goal

You can create a dictionary, add entries to it, look values up by key, recognise the KeyError a missing key raises, and test for a key with in.

In the lesson: Look at the example program spanish one and run it. It opens with the file's documentation string, three lines saying what the program does. Then the real work starts. First an empty dictionary is created using dict, and it is assigned the descriptive name spanish. Next come nine entries, one to a line, each pairing an English word with its Spanish translation. Finally, two look-ups print the definitions of two and of red. When we run it the shell shows dos, then rojo, and nothing else. Notice the shape of this program. Nine lines create the dictionary and two lines use it. Creating and using are quite different activities, and that difference is going to matter shortly.

## Files

- [`starter/spanish1.py`](starter/spanish1.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l01/m07l01-02/starter`
2. Read `spanish1.py` the way the lesson builds it:
   - Lines 1–4: the file's documentation string
   - Lines 5–6: an empty dictionary
   - Lines 7–15: nine entries
   - Lines 16–18: print the definitions of two
3. Notes from the lesson:
   - Line 6: dict() with nothing in the parentheses makes an empty dictionary
4. Run it: `python3 spanish1.py`.
5. Check it from the repository root: `./check m07l01-02`.

## Expected output

```text
dos
rojo
```

## How to check

`./check m07l01-02` copies `starter/` into a scratch directory and runs `python3 spanish1.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
