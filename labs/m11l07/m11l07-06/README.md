# m11l07-06 · From strings to numbers

**Lesson:** [Entry Objects](https://learnsome.tech/learn/python-course/m11l07) (lesson 11.7, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can put an Entry box in a graphics window with its own label, use a mouse click as the signal that typing has finished, and read or set its contents with getText and setText, converting to numbers where you need them.

In the lesson: The second Entry is almost identical code, which is a smell we will deal with shortly. Then the click, and then the part that matters. Just as with the input function, you can only read strings from an Entry. The names numStr one and numStr two are chosen to emphasise that. To do arithmetic you must convert, which is what the calls to int are for. Finally the two whole numbers are added. If the user typed something that is not a whole number, int raises a ValueError rather than quietly giving you nonsense.

## Files

- [`starter/addEntries.py`](starter/addEntries.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/addEntries.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: The second Entry is almost identical code
   - Lines 6–7: Then the click
   - Lines 8–10: which is what the calls to int are for
   - Lines 11–14: the two whole numbers are added

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l07-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l07) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
