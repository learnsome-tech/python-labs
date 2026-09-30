# m18l01-06 · The same file, imported instead of run

**Lesson:** [Modules And The Import System](https://learnsome.tech/learn/python-course/m18l01) (lesson 18.1, module 18: Organising Code) · Pro  
**Check:** Read along

## Goal

You can split code across files with import, explain what happens the first time a module is imported, protect a file's own test code with the main guard, and say where Python looked to find a module.

In the lesson: Now put a second file beside it. Report dot py imports greetings and calls one of its functions. Look at the two runs side by side. Run greetings itself and the name variable holds dunder main, so Ada is greeted. Run report and the loading line still appears, because it sits outside the guard and every import runs it, but this time the name variable holds the string greetings, the condition is false, and Ada is not greeted. That is the whole point of the guard. It lets one file be both a useful library for other files and a program you can run on its own, with its own tests or demonstration, without those going off in somebody else's face.

## Files

- [`starter/the-same-file-imported-instead-of-run.py`](starter/the-same-file-imported-instead-of-run.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/the-same-file-imported-instead-of-run.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m18l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m18l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
