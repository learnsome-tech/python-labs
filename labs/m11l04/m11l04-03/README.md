# m11l04-03 · The main program, and what it draws

**Lesson:** [Mutable Objects And Aliases](https://learnsome.tech/learn/python-course/m11l04) (lesson 11.4, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can explain why assigning one name from another gives two names for a single object, predict when mutating through one name is visible through the other, and use clone or a full slice to get a genuinely separate object.

In the lesson: The main function opens a three hundred by three hundred window and calls yUp, so that y grows upward the way it does in mathematics. Then it asks makeRect for a rectangle whose corner is at twenty, fifty, with a width of two hundred fifty and a height of two hundred. By that description the far corner lands at two hundred seventy, two hundred fifty, so the rectangle should fill most of the window. Draw it, then wait for a click to close. Run this yourself. What you get is not a big rectangle.

## Files

- [`starter/makeRectBad.py`](starter/makeRectBad.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/makeRectBad.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: opens a three hundred by three hundred window
   - Lines 3–6: asks makeRect for a rectangle
   - Lines 7–10: wait for a click to close

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
