# m11l01-04 · A Point, and why nothing happens yet

**Lesson:** [A Graphics Introduction](https://learnsome.tech/learn/python-course/m11l01) (lesson 11.1, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can open a graphics window, construct points, circles, lines and rectangles, colour them, draw them, move them and close the window, and you know why the vertical axis points the wrong way.

In the lesson: Next, a point. The point constructor takes an x coordinate and a y coordinate, here one hundred across and fifty down, and hands back a point object which the program gives a short name. Notice what does not happen: nothing appears in the window. You could have several graphics windows open at once, so you must always say which window a shape belongs to. Every graphical object has a draw method, and draw takes the window as its argument. Run the draw line and look hard at the window. The point shows as a single, small, black pixel.

## Files

- [`starter/graphIntro.py`](starter/graphIntro.py): the listing from the lesson
- [`starter/graphics.py`](starter/graphics.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/graphIntro.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: hands back a point object
   - Lines 9–10: Run the draw line

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
