# m18l02-08 · Running a module with dash m

**Lesson:** [Packages, And Your Own Library](https://learnsome.tech/learn/python-course/m18l02) (lesson 18.2, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can lay out a project as a package of modules with a script beside it, import between those modules with absolute imports, and run any module inside the package with the dash m switch.

In the lesson: There is a second way to run Python code, and it is the fix for that last error. Dash m takes a module name rather than a file path. Python imports it as part of its package and then runs it as the program. From the project folder, dash m weather dot report prints the same sentence, because the guard at the bottom of report fired, and this time the imports resolved properly. Try dash m on the package itself and Python tells you the package has no dunder main dot py, so it cannot be executed directly. Add such a file and it could. You have already used this switch without knowing: python dash m pip, and python dash m venv, which is the next lesson.

## Files

- [`starter/running-a-module-with-dash-m.txt`](starter/running-a-module-with-dash-m.txt): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/running-a-module-with-dash-m.txt` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l02-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
