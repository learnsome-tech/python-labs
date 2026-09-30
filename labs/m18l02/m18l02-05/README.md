# m18l02-05 · What dunder init dot py is for now

**Lesson:** [Packages, And Your Own Library](https://learnsome.tech/learn/python-course/m18l02) (lesson 18.2, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can lay out a project as a package of modules with a script beside it, import between those modules with absolute imports, and run any module inside the package with the dash m switch.

In the lesson: Now the file that puzzles everybody: dunder init dot py. Historically it was required, and a folder without one was not a package at all. Since version three point three Python can treat a plain folder as a package, so it is no longer mandatory, but write one anyway. Its presence says this folder is a package I control, and it gives you somewhere to put the package docstring. Empty is fine. The one real use is re-exporting: if init imports summary from report, then callers can write from weather import summary and never learn which module it lives in. That is a kindness for a library other people use. Keep the file small, because every line in it runs before anything else in the package can be imported.

## Files

- [`starter/what-dunder-init-dot-py-is-for-now.py`](starter/what-dunder-init-dot-py-is-for-now.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/what-dunder-init-dot-py-is-for-now.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
