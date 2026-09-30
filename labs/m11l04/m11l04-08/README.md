# m11l04-08 · The corrected program

**Lesson:** [Mutable Objects And Aliases](https://learnsome.tech/learn/python-course/m11l04) (lesson 11.4, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can explain why assigning one name from another gives two names for a single object, predict when mutating through one name is visible through the other, and use clone or a full slice to get a genuinely separate object.

In the lesson: Here is makeRect from makeRectangle, the corrected example. The only difference from the broken version is the call to clone, and the author has flagged it with a loud comment so that you cannot miss it. Everything else is untouched: move the clone by the width and the height, then build the Rectangle from the two corners. The main function is unchanged and is not on screen. Run it and you get the large rectangle the docstring promised. Take a moment to appreciate how small the difference is. A whole class of bugs comes down to one missing method call, and nothing in the broken version looked suspicious.

## Files

- [`starter/graphics.py`](starter/graphics.py)
- [`starter/makeRectangle.py`](starter/makeRectangle.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/makeRectangle.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: Here is makeRect from makeRectangle
   - Lines 7–11: the call to clone
   - Lines 12–13: build the Rectangle from the two corners
3. Notes from the lesson:
   - Line 11: clone makes the new Point, so corner is never disturbed

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l04-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
