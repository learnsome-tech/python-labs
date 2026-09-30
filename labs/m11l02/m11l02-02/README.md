# m11l02-02 · The standard starting lines

**Lesson:** [Sample Graphics Programs](https://learnsome.tech/learn/python-course/m11l02) (lesson 11.2, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can write a complete graphics program with the standard starting lines, build a picture from circles, lines, ovals, text and polygons, take input from mouse clicks, and close the window from inside the picture.

In the lesson: Immediately after the documentation string comes the import line. Always have it in a graphics program. Then the work happens inside a function called main, which is called at the bottom of the file. The first statement shows the general form of the graph win constructor: a window title, then a width and a height in pixels. The second turns the coordinate system right side up, so the vertical coordinate increases up the screen. That method is one of the tutorial's additions, and from then on every coordinate is in the new system. These are your standard opening lines; only the title and dimensions change.

## Files

- [`starter/face.py`](starter/face.py): the listing from the lesson
- [`starter/graphics.py`](starter/graphics.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/face.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: the import line
   - Lines 5–8: the general form
   - Lines 9: turns the coordinate system

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
