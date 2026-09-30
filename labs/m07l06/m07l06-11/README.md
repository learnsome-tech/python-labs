# m07l06-11 · One function, called twice in one line

**Lesson:** [Playing Computer](https://learnsome.tech/learn/python-course/m07l06) (lesson 7.6, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can trace a loop or a nest of function calls by hand, keeping one table row per executed line, and use that table to locate the exact line where a logical error appears.

In the lesson: The last of the three is the shortest, and the trickiest to trace. There is a definition of a function that adds four to whatever it is given, and one print statement that calls it twice and multiplies the two results together. Three lines of code will give you a table with a good many rows, because control leaves the print statement, runs the function, comes back, leaves again, and comes back again before the multiplication can happen.

## Files

- [`starter/playcompfunc.py`](starter/playcompfunc.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/playcompfunc.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: a definition of a function
   - Lines 3: one print statement

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l06-11` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
