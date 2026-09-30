# m18l02-07 · Relative imports, and why absolute wins

**Lesson:** [Packages, And Your Own Library](https://learnsome.tech/learn/python-course/m18l02) (lesson 18.2, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can lay out a project as a package of modules with a script beside it, import between those modules with absolute imports, and run any module inside the package with the dash m switch.

In the lesson: You will see imports beginning with a dot. A leading dot means from the package I am already in, so from dot readings import highest does the same job with less typing. It works, and it survives renaming the package. But it is fragile in one way that costs beginners an afternoon. Run that file directly as a program and Python says it attempted a relative import with no known parent package, because a file run as a program has no package to be relative to. The absolute version fails too, differently: it cannot find weather, because the folder on the search path is now the weather folder, not the project above it. Prefer absolute imports. They read the same wherever they appear, and a reader can find the file from the import alone.

## Files

- [`starter/relative-imports-and-why-absolute-wins.py`](starter/relative-imports-and-why-absolute-wins.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/relative-imports-and-why-absolute-wins.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l02-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
