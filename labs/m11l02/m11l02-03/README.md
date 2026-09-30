# m11l02-03 · A head and two different eyes

**Lesson:** [Sample Graphics Programs](https://learnsome.tech/learn/python-course/m11l02) (lesson 11.2, module 11: Graphics) · Pro  
**Check:** Read along

## Goal

You can write a complete graphics program with the standard starting lines, build a picture from circles, lines, ovals, text and polygons, take input from mouse clicks, and close the window from inside the picture.

In the lesson: Three shapes, each built the same way: construct, set a property, draw. The head is a circle with its centre given directly and a radius, filled yellow. Because of the earlier call that flipped the axis, a vertical coordinate of one hundred is above the middle of a window one hundred and fifty pixels high. One eye is a small blue circle. Notice the ordering: if the head were drawn after the eye, the eye would vanish, because the most recent thing drawn sits on top. The other eye is a line between two points, made three pixels thick.

## Files

- [`starter/face.py`](starter/face.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/face.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: The head is a circle
   - Lines 4–7: One eye
   - Lines 8–11: The other eye

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m11l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/python-course/m11l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
