# m10l01-08 · The finished cue finder

**Lesson:** [Mad Libs Revisited: Finding The Cues](https://learnsome.tech/learn/python-course/m10l01) (lesson 10.1, module 10: Mad Libs Revisited) · Pro  
**Check:** Read along

## Goal

You can write a function that scans a format string and returns the list of cues embedded in it, and you can follow the creative process that produced it.

In the lesson: Here is the whole function with every English phrase replaced by Python. The heading and the documentation string are as we planned them. Then come three initialisations: an empty list, end set to zero, and the number of repetitions from the count method. Inside the loop the first line finds the braces for the next key and steps one past the open one, the second finds the closing brace searching from the start of the key, the third takes the slice, and the fourth appends it to the list. After the loop, the return statement hands back the list. Watch how start, end, key and the list are all modified on every turn. Above the heading the file has a one line comment, which is off screen.

## Files

- [`starter/testGetKeys.py`](starter/testGetKeys.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/testGetKeys.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: The heading and the documentation string
   - Lines 4–7: three initialisations
   - Lines 8–10: finds the braces
   - Lines 11–12: appends it
   - Lines 13: hands back the list

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m10l01-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
