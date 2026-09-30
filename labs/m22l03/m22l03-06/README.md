# m22l03-06 · A linter finds real mistakes

**Lesson:** [Formatting, Linting And Style](https://learnsome.tech/learn/python-course/m22l03) (lesson 22.3, module 22: Testing, Typing And Shipping) · Pro  
**Check:** Read along

## Goal

You can name and lay out code the way the rest of the Python world does, let a formatter settle the arguments, read what a linter reports, and write a docstring worth reading.

In the lesson: A linter is different. It does not change your file; it reads it and complains, and what it complains about is not always cosmetic. Run ruff check on this file and it reports three things, each of a different kind. An import that is never used, which is clutter and sometimes a leftover from code you deleted. A variable that is assigned and never read, which usually means you meant to use it and did not. And, on the last line, a name that does not exist: ags, a typo for ages, which would crash every single time the function is called. A test would catch that. The linter caught it without running anything.

## Files

- [`starter/report.py`](starter/report.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/report.py` alongside the lesson.
2. Notes from the lesson:
   - Line 7: computed, never used: either use it or delete it
   - Line 8: a typo for ages: this line raises a name error every time

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m22l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m22l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
