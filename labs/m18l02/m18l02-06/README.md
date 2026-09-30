# m18l02-06 · The script that ties it together

**Lesson:** [Packages, And Your Own Library](https://learnsome.tech/learn/python-course/m18l02) (lesson 18.2, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can lay out a project as a package of modules with a script beside it, import between those modules with absolute imports, and run any module inside the package with the dash m switch.

In the lesson: Last comes main dot py, and it goes beside the package, not inside it. It is deliberately tiny: import the one function that matters and call it. Now run it from the project folder, and there is the sentence. Why does the absolute import work here? Because you ran main dot py, so the folder holding main dot py is the first entry on the search path, and the weather folder is sitting right there in it. That is the layout to copy: a thin script at the top, all the real work in a package next to it. When the script grows past twenty lines, that is a sign a new module wants to exist.

## Files

- [`starter/main.py`](starter/main.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/main.py` alongside the lesson.
2. Notes from the lesson:
   - Line 3: main.py sits beside the weather folder, not inside it

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
