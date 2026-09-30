# m11l05-04 · Two ways to import a module

**Lesson:** [Animation: Moving One Shape](https://learnsome.tech/learn/python-course/m11l05) (lesson 11.5, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can animate a single graphics object with a loop, a call to move and a call to time.sleep, explain why the delay and the drawing order matter, and turn a repeated animation loop into a reusable function.

In the lesson: The program uses two different import forms, and the difference is worth a minute. The time module is imported by name, so the sleep function is written as time dot sleep. Had we written from time import star, we could write sleep on its own, which is shorter but hides where sleep came from. Worse, two modules may define functions with the same name, and then one of them quietly wins. With the module prefix there is no ambiguity, so the form import moduleName is the safer and more typical one. If you doubt the scale of the problem, type help of the string modules in the Shell and wait a few seconds. The list is enormous.

## Files

- [`starter/graphics.py`](starter/graphics.py)
- [`starter/two-ways-to-import-a-module.py`](starter/two-ways-to-import-a-module.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/two-ways-to-import-a-module.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
