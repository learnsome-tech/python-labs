# m18l02-03 · The first module in the package

**Lesson:** [Packages, And Your Own Library](https://learnsome.tech/learn/python-course/m18l02) (lesson 18.2, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can lay out a project as a package of modules with a script beside it, import between those modules with absolute imports, and run any module inside the package with the dash m switch.

In the lesson: Build the package yourself. Make a folder called hello, and a folder called weather inside it. The first file in the package is readings dot py, and it holds the data at the top and two functions over it. Nothing here is new: a list, and two functions that return the highest and the mean. The one detail worth naming is that the list is written in capitals. That is a convention, not a rule: capitals say this value is set once when the module loads and nobody reassigns it. Notice also that this module imports nothing and knows nothing about the rest of the package. The modules at the bottom of a project usually look like that, and it is why they are easy to test.

## Files

- [`starter/readings.py`](starter/readings.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/readings.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: the data at the top
   - Lines 4–9: two functions over it
3. Notes from the lesson:
   - Line 3: capitals by convention: a value nobody reassigns

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
