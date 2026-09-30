# m18l02-04 · A module that imports its neighbour

**Lesson:** [Packages, And Your Own Library](https://learnsome.tech/learn/python-course/m18l02) (lesson 18.2, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can lay out a project as a package of modules with a script beside it, import between those modules with absolute imports, and run any module inside the package with the dash m switch.

In the lesson: The second module is report dot py, and it needs the first. The import names the full path from the top of the project: from weather dot readings, import average and highest. Then it builds one sentence out of them and returns it, printing nothing, as you learned to prefer. At the bottom it has its own guard, so this module can also be run on its own while you are working on it. Two files, one importing the other, each with a single job. That is the shape of every Python project you will ever read, repeated at whatever scale the project happens to be.

## Files

- [`starter/report.py`](starter/report.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/report.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: the full path from the top
   - Lines 4–6: builds one sentence
   - Lines 7–9: its own guard
3. Notes from the lesson:
   - Line 3: absolute: package, then module, then names
   - Line 8: so this module can also be run on its own

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
