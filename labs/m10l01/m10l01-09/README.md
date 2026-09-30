# m10l01-09 · The test story and the call

**Lesson:** [Mad Libs Revisited: Finding The Cues](https://learnsome.tech/learn/python-course/m10l01) (lesson 10.1, module 10: Mad Libs Revisited) · Pro  
**Check:** Read along

## Goal

You can write a function that scans a format string and returns the list of cues embedded in it, and you can follow the creative process that produced it.

In the lesson: The rest of the test file is the story and one call. The story is a triple quoted string, so it runs over many lines and keeps its line breaks, and the cues sit in braces: animal, food and city. At the bottom, the print call hands the story to getKeys and prints whatever comes back. Run the file and you see animal, animal, food, food, animal, food, animal, city, food, animal, food. That is eleven entries for three different cues, because the function reports every appearance, exactly as its documentation string promises. Whether that is what a mad lib program wants is a separate question, and the next module answers it.

## Files

- [`starter/testGetKeys.py`](starter/testGetKeys.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/testGetKeys.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–15: a triple quoted string
   - Lines 16–17: the print call

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m10l01-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
