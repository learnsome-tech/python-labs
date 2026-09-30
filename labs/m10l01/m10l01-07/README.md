# m10l01-07 · Make the first key fit the general code

**Lesson:** [Mad Libs Revisited: Finding The Cues](https://learnsome.tech/learn/python-course/m10l01) (lesson 10.1, module 10: Mad Libs Revisited) · Pro  
**Check:** Read along

## Goal

You can write a function that scans a format string and returns the list of cues embedded in it, and you can follow the creative process that produced it.

In the lesson: So the code that works for the second key, and every key after it, searches for the open brace onwards from the end of the previous key. Each turn of the loop uses the end left behind by the turn before. What about the first key, where there is no previous turn? We could write separate code for it, but there is a neater way: give end a starting value that makes the general code correct. The first search should begin at the very beginning of the string, which is index zero. So we set end to zero before the loop, and those same two lines then serve the first key and all the rest. Making the first turn fit the general pattern by initialising properly is a trick you will use again.

## Files

- [`starter/make-the-first-key-fit-the-general-code.py`](starter/make-the-first-key-fit-the-general-code.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/make-the-first-key-fit-the-general-code.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m10l01-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m10l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
