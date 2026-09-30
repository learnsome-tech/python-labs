# m11l01-11 · Printing objects for debugging, then closing

**Lesson:** [A Graphics Introduction](https://learnsome.tech/learn/python-course/m11l01) (lesson 11.1, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can open a graphics window, construct points, circles, lines and rectangles, colour them, draw them, move them and close the window, and you know why the vertical axis points the wrong way.

In the lesson: The tutorial's version of the module adds something Zelle's does not: every graphics object can be printed, and it produces a descriptive string. It shows position only, but position is usually what you are missing. When a shape is invisible because it is off the screen, or hidden underneath something else, three temporary lines like these are an excellent reality check. Then a comment inviting you to experiment, and remember you will not see the effect until you run the whole program again. The input call holds everything open, waiting in the shell. Finally the close method destroys the window; nothing else will.

## Files

- [`starter/graphIntro.py`](starter/graphIntro.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/graphIntro.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: can be printed
   - Lines 4–5: a comment inviting you
   - Lines 6–7: The input call holds
   - Lines 8–9: the close method destroys

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l01-11` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
