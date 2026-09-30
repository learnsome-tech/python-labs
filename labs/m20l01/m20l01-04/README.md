# m20l01-04 · Two instances keep their own data

**Lesson:** [Classes And Instances](https://learnsome.tech/learn/python-course/m20l01) (lesson 20.1, module 20: Object Oriented Python) · Pro  
**Check:** Graded

## Goal

You can write a class with an initialiser, create instances of it, store data on each instance, and explain the difference between the class and an instance of it.

In the lesson: The class is written once, and you can make as many instances from it as you like. Here two calls give us Fido, aged three, and Rex, aged seven. Each instance carries its own name and its own age, in its own storage. Now give it a birthday: assigning to fido dot age changes the age on that one dog and leaves Rex alone, and the printed line proves it. The next two answers are the ones to fix in your head. Fido is Rex is false, because these are not the same object. But the type of fido is the type of Rex is true, because both were built from the very same class. Same class, different objects, separate data.

## Files

- [`starter/dog2.py`](starter/dog2.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m20l01/m20l01-04/starter`
2. Read `dog2.py` the way the lesson builds it:
   - Lines 1–6: The class is written once
   - Lines 7–10: two calls
   - Lines 11–15: give it a birthday
3. Notes from the lesson:
   - Line 12: changing one instance leaves the other completely alone
   - Line 14: two different objects, so is gives False
4. Run it: `python3 dog2.py`.
5. Check it from the repository root: `./check m20l01-04`.

## Expected output

```text
Fido 3
Rex 7
4 7
False
True
```

## How to check

`./check m20l01-04` copies `starter/` into a scratch directory and runs `python3 dog2.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m20l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
