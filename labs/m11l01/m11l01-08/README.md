# m11l01-08 · A Line, and the tuple trap

**Lesson:** [A Graphics Introduction](https://learnsome.tech/learn/python-course/m11l01) (lesson 11.1, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can open a graphics window, construct points, circles, lines and rectangles, colour them, draw them, move them and close the window, and you know why the vertical axis points the wrong way.

In the lesson: A line object is constructed from two points. Here we reuse the point we already have as one end, and build a second point directly inside the constructor for the other end. Technically what you get is a segment between the two points. Now the trap, and it catches almost everyone. A bare pair of numbers in round brackets is a tuple in Python, and a tuple is not a point. The constructors for all the graphics objects want real point objects, so wrap the point constructor around the coordinates every time. Draw it, and a black segment runs down and to the right.

## Files

- [`starter/graphIntro.py`](starter/graphIntro.py): the listing from the lesson
- [`starter/graphics.py`](starter/graphics.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/graphIntro.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–18: A line object is constructed
   - Lines 19: Draw it
3. Notes from the lesson:
   - Line 18: Point(150, 100) is a Point; (150, 100) is a tuple, and will fail

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l01-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
