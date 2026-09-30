# m07l06-09 · Code with a mistake in it

**Lesson:** [Playing Computer](https://learnsome.tech/learn/python-course/m07l06) (lesson 7.6, module 7: Dictionaries And Loops) · Pro  
**Check:** Read along

## Goal

You can trace a loop or a nest of function calls by hand, keeping one table row per executed line, and use that table to locate the exact line where a logical error appears.

In the lesson: This function is supposed to compute the product of the numbers in a list. Given the list of five, four and six, the answer should be a hundred and twenty, reached in steps: five, then five times four is twenty, then twenty times six is a hundred and twenty. It does not do that. If the previous example has done its work you may already suspect which line is guilty, but suspecting is not the exercise. The exercise is to prove it from a table, and to see exactly where the data you expected gets mangled. The same code is in the example file called num product wrong.

## Files

- [`starter/playcomperror.py`](starter/playcomperror.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/playcomperror.py` alongside the lesson.
2. Notes from the lesson:
   - Line 5: the intended answer for [5, 4, 6] is 5, then 20, then 120

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l06-09` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m07l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
